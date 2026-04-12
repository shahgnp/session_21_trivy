## Deploying the image

### Step 1: Create a ID_RSA CI/CD Variable with following private key

<< THE PRIVATE KEY HAS BEEN REDACTED >>

### Step 2: To the previous pipeline add these things
variables:
  PORT: 8000

stages:
  - build
  - scan
  - deploy

# (Build and Scan stages remain the same as your previous lab)
# ... [Build Job] ...
# ... [Scan Job] ...

deploy_to_vm:
  stage: deploy
  image: alpine:latest
  script:
    - apk update && apk add --no-cache openssh-client

    # tr -d removes Windows returns
    # The 'echo >>' forces a newline at the end of the file
    - tr -d '\r' < $ID_RSA > cleaned_id_rsa
    - echo "" >> cleaned_id_rsa
    - chmod 600 cleaned_id_rsa

    # Debug step: Show the first line to confirm it looks like a key
    - head -n 1 cleaned_id_rsa

    - echo "Starting deployment on remote server 10.0.60.230..."
    - echo "Connecting to 10.0.60.230..."
    # Using SSH to run commands on the Target VM
    - |
      ssh -i cleaned_id_rsa -o StrictHostKeyChecking=no support@10.0.60.230  "

        # Pull the latest image
        docker pull $IMAGE_NAME

        # Stop and Remove the old container if it exists (using || true to ignore errors)
        docker stop flask-trivy-app-yourname || true
        docker rm flask-trivy-app-yourname || true

        # Start the new container
        docker run -d --name flask-trivy-app-yourname -p $PORT:5000 $IMAGE_NAME

        # Clean up unused images to save disk space
        docker image prune -f
      "
    - echo "Deployment Successful! 🚀"

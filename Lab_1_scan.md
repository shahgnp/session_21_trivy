## Create a pipeline with Trivy and SBOM

### Prerequisites
*   A **GitLab** account.
*   A **Docker Hub** account.
*   **Docker** installed on your local machine.
*   **Git** installed.

### Step 1: Create a local Git repo
Open your terminal and set up your project structure.
```bash
mkdir flask-trivy-app && cd flask-trivy-app
git init
```

### Step 2: Create a GitLab Repository
1. Log in to [GitLab.local](https://gitlab.local).
2. Click **New Project** > **Create empty project**.
3. Name it `flask-trivy-app` or anything.
4. Click **Create project**.

### Step 3: Add GitLab remote to the local repo
Copy the URL of your new GitLab project (the HTTPS version).
```bash
git remote add origin <YOUR_GITLAB_PROJECT_URL>
```

### Step 4: Create a Registry and PAT on Docker Hub

You need a place for your image to live and a secure way for GitLab to talk to Docker Hub.

    Create Repository:

        Log in to Docker Hub.

        Click Create Repository.

        Name it `flask-trivy-app-yourname`. Set it to Public.

    Create Personal Access Token (PAT):

        Click on your Profile Icon (top right) > Account Settings.

        Navigate to Security > Personal Access Tokens.

        Click Generate New Token.

        Description: gitlab-pipeline-token.

        Access Permissions: Read, Write, Delete.

        Copy the token immediately! (You won't see it again).

### Step 5: Configure GitLab CI/CD Variables

Crucial: Never put your Docker Hub password in your code. We store it securely in GitLab.

    In your GitLab Project, go to Settings (bottom left) > CI/CD.

    Expand the Variables section.

    Add two variables:

        Key: DOCKER_HUB_USER | Value: Your-Docker-Hub-Username

        Key: DOCKER_HUB_PWD | Value: Your-Docker-Hub-PAT-Generated-In-Step-3

        (Keep "Protect variable" and "Mask variable" checked for the password).

### Step 6: Create the Application Files
We need three files to make this a "Better Application": the code, the Docker instructions, and the Pipeline instructions.

**File 1: `app.py` (The Application)**

**File 2: `Dockerfile` (The Container Instructions)**
**File 3: `.gitlab-ci.yml` (The Pipeline Config)**
This file tells GitLab to build your Docker image and store it in its Container Registry.

### Step 7: Commit and Push
```bash
git add .
git commit -m "feat: initial app with docker and ci pipeline"
git branch -M main
git push -u origin main
```

### Step 8: Observe the Pipeline Execution
1. Go to your GitLab Project.
2. On the left sidebar, go to **Build** > **Pipelines**.
3. You will see a "Running" status. Click on it to see the logs.
4. Once the pipeline passes, log in to your Docker Hub account in your browser. You will see your new flask-app repository with a latest tag.
5. You should see your image listed there!
6. Analyse the job logs
7. Use https://www.prismor.dev/sbom-visualizer


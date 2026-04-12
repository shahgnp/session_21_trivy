from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.getenv('VERSION', '1.0.0')
    return f"<h1>Hello from GitLab CI!</h1><p>App Version: {version}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
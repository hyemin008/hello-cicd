from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    commit = os.environ.get("GIT_COMMIT", "local")
    return f"Hello from Jenkins! Commit: {commit}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

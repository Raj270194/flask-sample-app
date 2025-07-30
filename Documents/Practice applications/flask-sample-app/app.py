from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "local")
    return f"<h1>Welcome to Flask!</h1><p>App version: <strong>{version}</strong></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
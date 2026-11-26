import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>CI/CD Pipeline Demo - Version 1.0 is Live!</h1>"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

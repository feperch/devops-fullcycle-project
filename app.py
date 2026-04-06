from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "message": "Hello, DevOps!",
        "timestamp": datetime.datetime.now().isoformat(),
        "environment": os.getenv("ENV", "development"),
        "version": "1.0.0"
    }

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

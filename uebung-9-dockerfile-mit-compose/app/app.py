import os

from flask import Flask


app = Flask(__name__)


@app.get("/")
def home():
    return {
        "message": "Hallo aus Uebung 9",
        "service": "app",
        "redis_host": os.getenv("REDIS_HOST", "not-set"),
    }


if __name__ == "__main__":
    print(f"Starting app with REDIS_HOST={os.getenv('REDIS_HOST', 'not-set')}")
    app.run(host="0.0.0.0", port=5000)

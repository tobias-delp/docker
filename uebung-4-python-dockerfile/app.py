from flask import Flask


app = Flask(__name__)


@app.get("/")
def home():
    return {
        "message": "Hallo aus dem Flask-Container",
        "course": "Software Engineering",
        "topic": "Dockerfile lesen und verbessern",
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

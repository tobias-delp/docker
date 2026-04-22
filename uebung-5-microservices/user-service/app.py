from flask import Flask


app = Flask(__name__)


@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Ada"},
        {"id": 2, "name": "Linus"},
    ]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

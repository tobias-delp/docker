from flask import Flask


app = Flask(__name__)


@app.get("/orders")
def orders():
    return [
        {"id": 101, "total": 49.99, "status": "open"},
        {"id": 102, "total": 19.99, "status": "paid"},
    ]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

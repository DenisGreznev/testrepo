from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/about")
def about():
    return "This is a simple Flask app."

@app.route("/ping")
def ping():
    return "Pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Just changed, Hello World 🔥</h1>"


@app.route('/bye')
def bye():
    return "<h1>Bye!<h1>"


if __name__ == "__main__":
    app.run()

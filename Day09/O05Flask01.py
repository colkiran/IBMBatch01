
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> hello world </h1>"

@app.route("/<username>")
def user(username):
    return f"<h2> Greeting Mr.{username}, Welcome to FLASK programming </h2>"

if __name__ == '__main__':
    app.run(debug=True)

"""My Flask game."""
from flask import Flask
app = Flask(__name__)

@app.route("/")  # '/' root is home too
@app.route("/home")
def hello():
    return "<strong>Hello World!</strong>"


@app.route("/login")
def login():
    return "Login Area"


@app.route("/about")
def about():
    return 'About Us'


if __name__ == '__main__':
    app.run(debug=True)  # can set debug=True inside run function

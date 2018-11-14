"""My Flask game."""
from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Gilver Souza',
        'title': 'Flask Game 1',
        'content': 'First post content',
        'date_posted': 'November 10, 2018'
    },
    {
        'author': 'Alan Turing',
        'title': 'Flask Game 2',
        'content': 'Second post content',
        'date_posted': 'November 10, 1954'
    }
]


@app.route("/")  # '/' root is home too
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/login")
def login():
    return render_template('login.html', title='Sign Area')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)  # can set debug=True inside run function

#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display C <text>"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """display python <text>"""
    if text != "is cool":
        text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display number if int"""
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    """that render a template with number if int"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

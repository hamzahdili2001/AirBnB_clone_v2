#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with the states"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page with the state's id"""
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

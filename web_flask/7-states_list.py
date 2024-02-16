#!/usr/bin/python3
"""script that starts a Flask web application"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Function that removes the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page"""
    states = storage.all(State)
    dict_to_html = {value.id: value.name for value in states.values()}
    return render_template(
        "7-states_list.html", Table="States", items=dict_to_html
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

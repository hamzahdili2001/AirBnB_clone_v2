#!/usr/bin/python3
"""WebFlask module"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """render to 10-hbnb_filters.html"""
    all_states = storage.all(cls=State)
    all_amenities = storage.all(cls=Amenity)

    return render_template(
        "10-hbnb_filters.html",
        states=all_states,
        amenities=all_amenities,
    )


@app.teardown_appcontext
def close_storage(exception):
    """Close sqlalchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)

    return render_template(
        '10-hbnb_filters.html',
        states=states,
        cities=cities
    )


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
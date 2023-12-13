#!/usr/bin/python3
"""script that start a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Display_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Display_C(text):
    text.replace("_", " ")
    return "c {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def Display_python(text='is cool'):
    text.replace("_", " ")
    return "c {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

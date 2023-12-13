#!/usr/bin/python3
"""script that start a Flask web application"""
from flask import Flask, render_template_string
import html


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
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def Display_python(text='is cool'):
    text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return '{} is a number'.format(html.escape(str(n)))


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    if isinstance(n, int):
        return render_template_string(
            '<html><body><h1>Number: {{ num }}</h1></body></html>',
            num=n
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

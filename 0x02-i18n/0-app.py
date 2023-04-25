#!/usr/bin/env python3

"""
module for a basic Flask app
contains a single / route
"""

from flask import Flask, render_template as render


app: Flask = Flask(__name__)


@app.route('/')
def home() -> str:
    """
    route which renders an index.html template
    args:   None
    return: `Hello world`: str (as header (<h1>))
    """
    return render('0-index.html', title='Welcome to Holberton', h1='Hello world')


if __name__ == '__main__':
    """
    starts the Flask application server
    debug set to True for hot/live reloading
    """
    app.run(debug=True)

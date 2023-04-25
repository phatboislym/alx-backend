#!/usr/bin/env python3

"""
module for a basic Flask app which contains a single / route
"""

from flask import Flask, render_template as render, request
from flask_babel import Babel
from typing import Union

app: Flask = Flask(__name__)
babel = Babel(app)


class Config():
    """
    class `Config` for Flask app configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    get_locale function 
    args:   None
    return: str | None
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """
    route which renders an index.html template
    args:   None
    return: `Hello world`: str (as header (<h1>))
    """
    return render('2-index.html')


if __name__ == '__main__':
    """
    starts the Flask application server
    debug set to True for hot/live reloading
    """
    app.run(debug=True)

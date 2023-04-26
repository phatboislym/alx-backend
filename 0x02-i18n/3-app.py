#!/usr/bin/env python3

"""
module contains:
    `app`: basic flask app
    `Config`: class for flask configuration
    `get_locale`: function matches text with supported languages
"""

from flask import Flask, render_template as render, request
from flask_babel import Babel
from typing import Union

app: Flask = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config(object):
    """
    class `Config` for Flask app configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    get_locale method
    args:   None
    return: str | None
    """
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'fr'


@app.route('/')
def home() -> str:
    """
    route which renders an index.html template
    args:   None
    return: `home_title`: str (as title (<title>))
            `home_header`: str (as header (<h1>))
    """
    return render('3-index.html')


if __name__ == '__main__':
    """
    starts the Flask application server
    debug set to True for hot/live reloading
    """
    app.run(debug=True)

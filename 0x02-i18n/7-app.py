#!/usr/bin/env python3

"""
module contains:
    `app`: basic flask app
    `Config`: class for flask configuration
    `get_locale`: function matches text with supported languages
    `get_timezone`
"""

from babel.dates import get_timezone as babel_get_timezone, timezone_selector
from flask import Flask, render_template as render, request
from flask_babel import Babel
import pytz
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
    if (request.args['locale'] in app.config['LANGUAGES']):
        return request.args['locale']
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@timezone_selector
def get_timezone() -> str:
    """
    Return the user's preferred timezone based on the following rules:
        1. Find timezone parameter in URL parameters
        2. Find timezone from user settings
        3. Default to UTC
    args:   None
    return: timezone: str
    """
    timezone: Union[str, None] = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            timezone = 'UTC'
        return (timezone)

    if request.user:
        timezone = request.user.timezone
        if (timezone):
            try:
                pytz.timezone(timezone)
            except pytz.exceptions.UnknownTimeZoneError:
                timezone = 'UTC'
            return (timezone)
    return ('UTC')


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

#!/usr/bin/env python3

"""
module contains:
    `app`: basic flask app
    `Config`: class for flask configuration
    `get_locale`: function matches text with supported languages
"""

from flask import Flask, g, render_template as render, request
from flask_babel import Babel
from typing import Dict, Union

app: Flask = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    class `Config` for Flask app configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'


app.config.from_object(Config)


def get_user(user_id) -> Union[Dict, None]:
    user = users.get(user_id)
    if user:
        return user
    return None


@app.before_request
def before_request():
    g.user = None
    if 'login_as' in request.args:
        user_id = int(request.args['login_as'])
        g.user = get_user(user_id)


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

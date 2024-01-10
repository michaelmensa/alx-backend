#!/usr/bin/env python3
'''
Module 4-app.py
'''
from flask_babel import Babel, _
from flask import Flask, render_template, request, g


class Config():
    ''' config class for configurations '''

    LANGUAGES = ['en', 'fr']

    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    ''' method to determine the best match for
    supported languages '''
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    ''' index route '''
    return render_template('5-index.html')


def get_user(user_id):
    ''' function to get user from mock users '''
    return users.get(user_id)


@app.before_request
def before_request():
    ''' before request function '''
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)


if __name__ == '__main__':
    app.run(debug=True)

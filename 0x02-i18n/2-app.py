#!/usr/bin/env python3
'''
Module 2-app.py
'''
from flask_babel import Babel
from flask import Flask, render_template, request


class Config():
    ''' config class for configurations '''

    LANGUAGES = ['en', 'fr']

    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.locale_selector
def get_locale():
    ''' method to determine the best match for
    supported languages '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])
        


@app.route('/')
def index():
    ''' index route '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)

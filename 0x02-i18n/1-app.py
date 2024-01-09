#!/usr/bin/env python3
'''
Module 1-app.py
'''
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    ''' index route '''
    return render_template('1-index.html')


class Config():
    ''' config class for configurations '''

    LANGUAGES = ['en', 'fr']

    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')

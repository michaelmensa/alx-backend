#!/usr/bin/env python3
'''
Module 0-app.py
'''
from flask import FlaskI, render_template


app = Flask(__name__)


@app.route('/')
def index() -> None:
    ''' index route '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()

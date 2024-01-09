#!/usr/bin/env python3
'''
Module 0-app.py
'''
from flask import FlaskI, render_template


app = Flask(__name__)


@app.routes('/')
def index():
    ''' index route '''
    return render_template('0-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run()

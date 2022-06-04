#!/usr/bin/python3
""" Flask app """

from flask import Flask
from models import storage

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """index page"""
    return 'Hello Flask'

if __name__ == '__main__':
    app.run(debug=True)

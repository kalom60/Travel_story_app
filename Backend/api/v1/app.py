#!/usr/bin/python3
"""flask instance"""

from flask import Flask, make_response, jsonify
from models import storage

app = Flask(__name__)

@app.errorhandler(404)
def error(error):
    """Handle error"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.teardown_appcontext
def close(exception):
    """Close session"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True)

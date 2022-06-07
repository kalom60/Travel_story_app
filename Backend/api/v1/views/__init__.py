#!/usr/bin/python3
"""create Blueprint"""

from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/api/v1')

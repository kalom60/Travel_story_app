#!/usr/bin/python3
"""create Blueprint"""

from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/api/v1')

from api.v1.views.user import *
from api.v1.views.story import *

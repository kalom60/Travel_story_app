#!/usr/bin/python3
"""create user API routes"""

from api.v1.views import views
from flask import jsonify
from models.user import User
from models import storage

@views.route('/users', methods=['GET'], strict_slashes=False)
def user():
    """return all users"""
    users = []
    for user in storage.all(User).values():
        users.append(user.to_dict())
    print(users)
    return jsonify(users)

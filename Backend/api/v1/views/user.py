#!/usr/bin/python3
"""create user API routes"""

from api.v1.views import views
from flask import jsonify, abort
from models.user import User
from models import storage

@views.route('/users', methods=['GET'], strict_slashes=False)
def user():
    """return all users"""
    users = []
    for user in storage.all(User).values():
        users.append(user.to_dict())
    return jsonify(users)

@views.route('/user/<id>', methods=['GET'], strict_slashes=False)
def find_user(id):
    """return a specific user based on id"""
    user = []
    for usr in storage.all(User).values():
        usr = usr.to_dict()
        if id == usr['id']:
            user.append(usr)
    if len(user) == 0:
        return abort(404)
    return jsonify(user)

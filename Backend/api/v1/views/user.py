#!/usr/bin/python3
"""create user API routes"""

from api.v1.views import views
from flask import jsonify, abort, make_response, request
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

@views.route('/user/<id>', methods=['DELETE'], strict_slashes=False)
def del_user(id):
    """deletes a specific user based on id"""
    for k, v in storage.all(User).items():
        if id in k:
            storage.delete(v)
            storage.save()
            return make_response(jsonify({}), 200)
    return abort(404)

@views.route('/user', methods=['POST'], strict_slashes=False)
def post_user():
    """create a user"""
    if not request.get_json():
        abort(400, description="Not a json")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    if 'username' not in request.get_json():
        abort(400, description="Missing username")

    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    new_obj = request.get_json()
    user = User(**new_obj)
    obj = user.to_dict()
    user.save()
    return make_response(jsonify(obj), 201)

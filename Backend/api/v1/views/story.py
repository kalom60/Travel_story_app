#!/usr/bin/python3
"""create a story API route"""

from api.v1.views import views
from flask import jsonify, abort, make_response, request
from models.story import Story
from models import storage

@views.route('/story', methods=['GET'], strict_slashes=False)
def all_story():
    """return all story instances"""
    story = []
    for post in storage.all(Story).values():
        story.append(post.to_dict())
    return jsonify(story)

@views.route('/story/<id>', methods=['GET'], strict_slashes=False)
def find_story(id):
    """return a specific story based on id"""
    for post in storage.all(Story).values():
        post = post.to_dict()
        if id == post['id']:
            return jsonify(post)
    return abort(404)

@views.route('/story/<id>', methods=['DELETE'], strict_slashes=False)
def del_story(id):
    """delete a specific story based on id"""
    for k, v in storage.all(Story).items():
        if id in k:
            storage.delete(v)
            storage.save()
            return make_response(jsonify({}), 200)
    return abort(404)

@views.route('/story', methods=['POST'], strict_slashes=False)
def post_story():
    """create a story instance"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'title' not in request.get_json():
        abort(400, description="Missing title")

    if 'Country' not in request.get_json():
        abort(400, description="Missing Country")

    if 'story' not in request.get_json():
        abort(400, description="Missing story")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    new_obj = request.get_json()
    story = Story(**new_obj)
    obj = story.to_dict()
    story.save()
    return make_response(jsonify(obj), 201)

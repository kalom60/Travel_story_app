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
    for posts in storage.all(Story).values():
        posts = posts.to_dict()
        if id == posts['id']:
            return jsonify(posts)
    return abort(404)

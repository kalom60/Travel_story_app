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

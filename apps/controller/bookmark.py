# -*- coding: utf-8 -*-
from flask import request, session, jsonify
from apps import db
from apps.models import Actor, Video, Favorite, Bookmark

def actor_bookmark():
    name = request.form.get('name')
    actor = Actor.query.get(name)
    email = session['session_user_email']
    bookmark = actor.favorite_actor.filter_by(userEmail=email).first()

    if bookmark:
        return jsonify(success=True)

    my_bookmark = Favorite(
        actorName=name,
        userEmail=email
    )
    db.session.add(my_bookmark)
    db.session.commit()

    return jsonify(success=True)


def video_bookmark():
    name = request.form.get('name')
    video = Video.query.get(name)
    email = session['session_user_email']
    bookmark = video.bookmark_video.filter_by(userEmail=email).first()

    if bookmark:
        return jsonify(success=True)

    my_bookmark = Bookmark(
        videoName=name,
        userEmail=email
    )
    db.session.add(my_bookmark)
    db.session.commit()

    return jsonify(success=True)

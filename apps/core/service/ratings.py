# -*- coding:utf-8 -*-
__author__ = 'bebop'
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response, \
    current_app, logging
from apps import app, db
from apps.core.model.models import Actor, Filmo, Rating, Bookmark
from apps.core.model import models as models


def save_star():

    star = int( request.form.get('star') )
    name =  request.form.get('name')

    video_detail = models.Video.query.get(name)
    email = session['session_user_email']

    connect_actor= video_detail.video_actor.all()
    rating_exist = video_detail.video_rating.filter(models.Rating.user_rating == email).first()

    if rating_exist: # 이미 평점을 매겼었음
        video_detail.score_total += star - rating_exist.rating

        for each in connect_actor:
            models.Actor.query.get(each.actor_name).score +=star - rating_exist.rating

        rating_exist.rating = star

    else: # 평점을 매긴 적이 없음
        rating = models.Rating(
        video_rating = video_detail.name,
        user_rating = email,
        rating = star)

        video_detail.score_count += 1
        video_detail.score_total += star

        for each in connect_actor:
            models.Actor.query.get(each.actor_name).score += star
            models.Actor.query.get(each.actor_name).count += 1 

        db.session.add(rating)

    db.session.commit()

    return jsonify(success=True, average = float(video_detail.score_total) / video_detail.score_count, count = video_detail.score_count)

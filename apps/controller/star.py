# -*- coding: utf-8 -*-
from flask import request, session, jsonify
from apps import db
from apps.models import  Actor, Video, RatingActor, RatingVideo, User
import math

def video_save_star():
    star = int(request.form.get('star'))
    if star <= 0:
        return jsonify(success=True)
    else:
        star = star % 6
    name = request.form.get('name')
    video = Video.query.get(name)
    email = session['session_user_email']
    rating = video.ratingVideo_video.filter_by(userEmail=email).first()
    if rating:  # 이미 평점을 매겼었음
        video.score += star - rating.rating
        a = float(video.score / video.count)
        video.average = float(math.ceil(a * 100) / 100)
        rating.rating = star
        db.session.commit()
    else:  # 평점을 매긴 적이 없음
        rating = RatingVideo(
            videoName=video.name,
            userEmail=email,
            rating=star)
        video.count += 1
        video.score += star
        a = float(video.score / video.count)
        video.average = float(math.ceil(a * 100) / 100)
        #영상평가갯수 db에 1추가
        User.query.get(email).numVideo += 1
        db.session.add(rating)
        db.session.commit()

    return jsonify(success=True)



def actor_save_star():
    star = int(request.form.get('star'))
    if star <= 0:
        return jsonify(success=True)
    else:
        star = star % 6
    name = request.form.get('name')
    actor = Actor.query.get(name)
    email = session['session_user_email']
    rating = actor.ratingActor_actor.filter_by(userEmail=email).first()

    if rating:  # 이미 평점을 매겼었음
        actor.score += star - rating.rating
        a = float(actor.score / actor.count)
        actor.average = float(math.ceil(a * 100) / 100)
        rating.rating = star
        db.session.commit()
    else:  # 평점을 매긴 적이 없음
        rating = RatingActor(
            actorName=actor.name,
            userEmail=email,
            rating=star)
        actor.count += 1
        actor.score += star
        a = float(actor.score / actor.count)
        actor.average = float(math.ceil(a * 100) / 100)
        #배우평가갯수 db에 1추가
        User.query.get(email).numActor +=1
        db.session.add(rating)
        db.session.commit()

    return jsonify(success=True)

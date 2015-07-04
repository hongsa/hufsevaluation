# -*- coding: utf-8 -*-
import math

from flask import redirect, url_for, render_template,flash, session, current_app
from sqlalchemy import desc
from apps.models import Actor,User,ActorReview,RatingActor,Video,VideoReview,RatingVideo
import random
from  sqlalchemy.sql.expression import func
import time,logging,json

def getMicrotime():
    return time.time()
#
def timeLogger(message, startTime, endTime):
    sMessage = message + " :: " + str( endTime - startTime )
    logging.error( sMessage)

def main_page():
    # 로그인 안한 상태로 오면 index로 빠꾸
    _s = getMicrotime()
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    random_actor = Actor.query.order_by(func.rand()).limit(6)
    random_video = Video.query.order_by(func.rand()).limit(6)

    actorRank1 = Actor.query.filter(Actor.count>5).order_by(desc(Actor.average)).limit(6)
    actorRank2 = Actor.query.order_by(desc(Actor.count)).limit(6)


    videoRank1 = Video.query.filter(Video.count>5).order_by(desc(Video.average)).limit(6)
    videoRank2= Video.query.order_by(desc(Video.count)).limit(6)

    email = session['session_user_email']
    user = User.query.get(email)
    rating1 = user.ratingActor_user
    rating2 = user.ratingVideo_user


    list_actor = []
    for i in actorRank1 and actorRank2:
        list_actor.append(i.name)

    rating_actor=[]
    for r in rating1:
        if r.actorName in list_actor:
            rating_actor.append(dict(name = r.actorName, rating=r.rating))


    list_video = []
    for v in videoRank1 and videoRank2:
        list_video.append(v.name)

    rating_video=[]
    for r in rating2:
        if r.videoName in list_video:
            rating_video.append(dict(name = r.videoName, rating=r.rating))

    number = random.randint(1,3)

    _e = getMicrotime()
    timeLogger(" main", _s, _e)

    return render_template("defaultPage.html", actorRank1=actorRank1,actorRank2=actorRank2,videoRank1=videoRank1,videoRank2=videoRank2,
                           number=number,rating_actor=rating_actor,rating_video=rating_video,random_actor=random_actor,random_video=random_video)


def review_actor():

    review_actor = ActorReview.query.order_by(desc(ActorReview.id)).limit(20)
    review=[]

    for each in review_actor:
        review.append(dict(r_name = each.actorName,content=each.content))

    return json.dumps(review)

def review_video():
    review_video = VideoReview.query.order_by(desc(VideoReview.id)).limit(20)

    review=[]

    for each in review_video:
        review.append(dict(r_name = each.videoName,content=each.content))

    return json.dumps(review)

def star_actor():

    star_actor = RatingActor.query.order_by(desc(RatingActor.id)).limit(20)
    star=[]

    for each in star_actor:
        star.append(dict(nick = each.user.nickname,rating = each.rating, s_name = each.actorName))

    return json.dumps(star)

def star_video():

    star_video = RatingVideo.query.order_by(desc(RatingVideo.id)).limit(20)
    star=[]
    for each in star_video:
        star.append(dict(nick = each.user.nickname,rating = each.rating, s_name = each.videoName))

    return json.dumps(star)

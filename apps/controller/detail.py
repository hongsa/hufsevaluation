# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, request, flash, session
from apps import db
from apps.models import User, Actor, Video, ActorReview, VideoReview
from apps import recommendation
import json

def actorDetail(name):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    # 해당하는 배우추출
    actorRow = Actor.query.get(name)

    #출연작품 가져오기
    appearVideo = actorRow.videos()
    #댓글 가져오기
    comments = actorRow.reviews()

    actors = recommendation.transformPrefs(recommendation.makePrefs())
    sList = recommendation.topMatches(actors,name)

    rating = actorRow.ratingActor_actor.filter_by(userEmail=email).first()
    if rating:
        return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments,rating=rating.rating,sList=sList)


    return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments,sList=sList)


#댓글입력

def actor_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)
            sUser=user.nickname
            sComment = request.form['comment']
            sName = request.form['actorName']
            thisComment={}
            thisComment=ActorReview(
            actorName=sName,
            userEmail=session['session_user_email'],
            content=sComment
            )
        #댓글 DB에 저장
            jsonDict = {}
            jsonDict['user']=sUser
            jsonDict['comments'] = sComment
            jsonDict['actorName'] = sName
            db.session.add(thisComment)
            db.session.commit()

            return json.dumps(jsonDict)

    except Exception, e:
        print " Occuring Exception. ", e


def videoDetail(name):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    # 해당하는 배우추출
    videoRow = Video.query.get(name)

    #출연작품 가져오기
    appearActor = videoRow.actors()
    #댓글 가져오기
    comments = videoRow.reviews()

    movies = recommendation.transformPrefs(recommendation.makePrefs())
    sList = recommendation.topMatches(movies,name)

    rating = videoRow.ratingVideo_video.filter_by(userEmail=email).first()
    if rating:
        return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments,rating=rating.rating, sList=sList)


    return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments,sList=sList)

#댓글입력
def video_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)

            sUser=user.nickname
            sComment = request.form['comment']
            sName = request.form['videoName']
            thisComment={}
            thisComment=VideoReview(
            videoName=sName,
            userEmail=session['session_user_email'],
            content=sComment
            )
        #댓글 DB에 저장
            jsonDict = {}
            jsonDict['user'] = sUser
            jsonDict['comments'] = sComment
            jsonDict['videoName'] = sName
            db.session.add(thisComment)
            db.session.commit()

            return json.dumps(jsonDict)

    except Exception, e:
        print " Occuring Exception. ", e

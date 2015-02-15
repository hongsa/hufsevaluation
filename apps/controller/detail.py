# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, request, flash, session
from apps import db
from apps.models import User, Actor, Video, ActorReview, VideoReview
from apps import recommendation
import json
import logging

def actorDetail(name):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))
    email = session['session_user_email']
    user = User.query.get(email)
    # 해당하는 배우추출
    actorRow = Actor.query.get(name)
    #출연작품 가져오기
    appearVideo = actorRow.videos()
    #댓글 가져오기
    comments = actorRow.reviews()

    # 유사작품 가져오기
    if actorRow.ratingActor_actor.count()>4:
        if not actorRow.prefs:
            actorRow.rated = actorRow.ratingActor_actor.count()
            db.session.commit()
            
            itemPrefs = recommendation.simActorPrefs()
            list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
            a = json.dumps(list)
            actorRow.prefs = a
            db.session.commit()
        sList = json.loads(actorRow.prefs)

    else:
        sList = False

    list = actorRow.actorReview_actor.filter_by(userEmail=email).with_entities(ActorReview.id).all()

    #별점 있는 지 확인
    rating = actorRow.ratingActor_actor.filter_by(userEmail=email).first()
    if rating:
        return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments,rating=rating.rating,list=list,sList=sList)
    else:
        return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments,list=list,sList=sList)


#댓글입력

def actor_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)
            sUser=user.nickname
            numActor = user.numActor
            if numActor<50:
                sLevel= 0
            elif 50<=numActor<100:
                sLevel= 1
            elif 100<=numActor<200:
                sLevel= 2
            elif 200<=numActor<400:
                sLevel= 3
            else:
                sLevel= 4
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
            jsonDict['level']=sLevel
            jsonDict['comments'] = sComment
            jsonDict['actorName'] = sName
            db.session.add(thisComment)
            db.session.commit()

            return json.dumps(jsonDict)

    except Exception, e:
        print " Occuring Exception. ", e


def a_comment_delete(id):

    if request.method =="GET":
        comment = ActorReview.query.get(id)
        name = comment.actorName
        db.session.delete(comment)
        db.session.commit()


        return redirect(url_for("actorDetail",name=name))


def videoDetail(name):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    user = User.query.get(email)
    # 해당하는 배우추출
    videoRow = Video.query.get(name)

    #출연작품 가져오기
    appearActor = videoRow.actors()
    #댓글 가져오기
    comments = videoRow.reviews()

    # 유사작품 가져오기
    if videoRow.ratingVideo_video.count()>4:
        if not videoRow.prefs:
            videoRow.rated = videoRow.ratingVideo_video.count()
            db.session.commit()

            itemPrefs = recommendation.simVideoPrefs()
            list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
            a = json.dumps(list)
            videoRow.prefs = a
            db.session.commit()
        sList = json.loads(videoRow.prefs)
    else:
        sList = False

    list = videoRow.videoReview_video.filter_by(userEmail=email).with_entities(VideoReview.id).all()

    rating = videoRow.ratingVideo_video.filter_by(userEmail=email).first()
    if rating:
        return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments,rating=rating.rating,list=list,sList=sList)
    return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments,list=list,sList=sList)

#댓글입력
def video_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)
            sUser=user.nickname
            numVideo = user.numVideo
            if numVideo<50:
                sLevel= 0
            elif 50<=numVideo<100:
                sLevel= 1
            elif 100<=numVideo<200:
                sLevel= 2
            elif 200<=numVideo<400:
                sLevel= 3
            else:
                sLevel= 4
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
            jsonDict['level'] = sLevel
            jsonDict['comments'] = sComment
            jsonDict['videoName'] = sName
            db.session.add(thisComment)
            db.session.commit()

            return json.dumps(jsonDict)

    except Exception, e:
        print " Occuring Exception. ", e


def v_comment_delete(id):

    if request.method =="GET":
        comment = VideoReview.query.get(id)
        name = comment.videoName
        db.session.delete(comment)
        db.session.commit()


        return redirect(url_for("videoDetail",name=name))
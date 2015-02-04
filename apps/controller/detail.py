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

    actors = recommendation.transformPrefs(recommendation.makePrefsActor())
    #유사배우 가져오기
    if actorRow.ratingActor_actor.count() == 0:
        return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments)

    else:
        sList = recommendation.topMatches(actors,name)


    mycomment = actorRow.actorReview_actor.filter_by(userEmail=email).all()

    list=[]
    for each in mycomment:
        list.append(each.id)


    #별점 있는 지 확인
    rating = actorRow.ratingActor_actor.filter_by(userEmail=email).first()

    if rating:
        return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments,rating=rating.rating,sList=sList,list=list)


    return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments,sList=sList,list=list)


#댓글입력

def actor_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)
            sUser=user.nickname
            sLevel=user.level
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
    movies = recommendation.transformPrefs(recommendation.makePrefs())
    if videoRow.ratingVideo_video.count()==0:
        # sList = ['해당 영상에 대한 평가가 필요합니다']
        return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments)
    else:
        sList = recommendation.topMatches(movies,name)

    mycomment = videoRow.videoReview_video.filter_by(userEmail=email).all()

    list=[]
    for each in mycomment:
        list.append(each.id)

    rating = videoRow.ratingVideo_video.filter_by(userEmail=email).first()

    if rating:
        return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments,rating=rating.rating, sList=sList,list=list)

    return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments,sList=sList,list=list)

#댓글입력
def video_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)

            sUser=user.nickname
            sLevel=user.level
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
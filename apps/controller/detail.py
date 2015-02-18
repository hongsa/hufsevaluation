# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, request, flash, session
from apps import db
from apps.models import User, Actor, Video, ActorReview, VideoReview,Filmo
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
    oFilmo = Filmo.query.filter_by(ActorName=name).all()

    #댓글 가져오기
    comments = actorRow.reviews()

    #유사배우 목록 가져오기
    sList = False
    successful=False
    try:
        #.prefs가 있을때
        if actorRow.prefs:
            successful=True
        else:
            if actorRow.count>4:
                try: #.prefs 값을 넣자
                    itemPrefs = recommendation.simActorPrefs()
                    list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
                    a = json.dumps(list)
                    actorRow.prefs = a
                    db.session.commit()
                    successful=True
                except: pass
            else:pass
    except:pass
    if successful:
        oList = json.loads(actorRow.prefs)
        if len(oList) >1:
            sList = oList[0:-1]

    list = actorRow.actorReview_actor.filter_by(userEmail=email).with_entities(ActorReview.id).all()

    #별점 있는 지 확인
    # rating = actorRow.ratingActor_actor.filter_by(userEmail=email).first()
    rating = user.ratingActor_user.filter_by(actorName=name).first()
    if rating:
        return render_template("actorDetail.html", actorRow=actorRow, oFilmo=oFilmo, comments=comments,rating=rating.rating,list=list,sList=sList)
    else:
        return render_template("actorDetail.html", actorRow=actorRow, oFilmo=oFilmo, comments=comments,list=list,sList=sList)


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
    oFilmo = Filmo.query.filter_by(videoName=name).all()
    appearActor = []
    #댓글 가져오기
    comments = videoRow.reviews()

    #유사영상 목록 가져오기
    sList = False
    successful=False
    try:
        #값도 있고 그 값이 비교적 최신인 경우 (10개 평가마다 갱신) (완벽한 조건)
        if videoRow.prefs:
            successful=True
        else:
            #DB에 값들을 확인하는 참회의 시간을 가져보자.
            if videoRow.count>4: #평가수가 충분한 경우. 평가수 부족하면 바로 OUT
                try: #.prefs 값을 넣자
                    itemPrefs = recommendation.simVideoPrefs()
                    list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
                    a = json.dumps(list)
                    videoRow.prefs = a
                    db.session.commit()
                    successful=True
                except:pass
            else: pass #평가수가 부족하니까 OUT
    except:pass
    if successful:
        oList = json.loads(videoRow.prefs)
        if len(oList)>1:
            sList = oList[0:-1]

    list = videoRow.videoReview_video.filter_by(userEmail=email).with_entities(VideoReview.id).all()

    # rating = videoRow.ratingVideo_video.filter_by(userEmail=email).first()
    rating = user.ratingVideo_user.filter_by(videoName=name).first()
    if rating:
        return render_template("videoDetail.html", videoRow=videoRow, oFilmo=oFilmo, comments=comments,rating=rating.rating,list=list,sList=sList)
    return render_template("videoDetail.html", videoRow=videoRow, oFilmo=oFilmo, comments=comments,list=list,sList=sList)

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
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
    # user = User.query.get(email)
    # 해당하는 배우추출
    actorRow = Actor.query.get(name)
    #출연작품 가져오기
    appearVideo = actorRow.videos()
    #댓글 가져오기
    comments = actorRow.reviews()

    #유사배우 목록 가져오기
    sList = False
    successful=False
    try:
        #값도 있고 그 값이 비교적 최신인 경우 (10개 평가마다 갱신) (완벽한 조건)
        if actorRow.prefs and actorRow.ratingActor_actor.count() < actorRow.rated +10:
            successful=True
        else:
            #DB에 값들을 확인하는 참회의 시간을 가져보자.
            if actorRow.ratingActor_actor.count()>4: #평가수가 충분한 경우. 평가수 부족하면 바로 OUT
                if (not actorRow.rated > 4):#평가 수는 충분한데 그 값이 DB에 업데이트되지 않은 경우 or NULL값인경우
                    try: #업데이트 시켜주자
                        actorRow.rated = actorRow.ratingActor_actor.count()
                        db.session.commit()
                    except: pass
                #그럼 이제 .rated는 다 있는거다.
                if not actorRow.prefs:
                    try: #.prefs 값을 넣자
                        itemPrefs = recommendation.simActorPrefs()
                        list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
                        a = json.dumps(list)
                        actorRow.prefs = a
                        db.session.commit()
                        successful=True
                    except: pass
                try:
                    #값이 최신으로 업데이트 되지 않았을 때
                    if actorRow.ratingActor_actor.count()>=actorRow.rated +10:
                        try:
                            actorRow.rated = actorRow.ratingActor_actor.count()
                            db.session.commit()
                            itemPrefs = recommendation.simActorPrefs()
                            list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
                            a = json.dumps(list)
                            actorRow.prefs = a
                            db.session.commit()
                            successful=True
                        except: pass
                except:pass
            else: pass #평가수가 부족하니까 OUT
    except:pass
    if successful:
        sList = json.loads(actorRow.prefs)

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
    # user = User.query.get(email)
    # 해당하는 배우추출
    videoRow = Video.query.get(name)

    #출연작품 가져오기
    appearActor = videoRow.actors()
    #댓글 가져오기
    comments = videoRow.reviews()

    #유사영상 목록 가져오기
    sList = False
    successful=False
    try:
        #값도 있고 그 값이 비교적 최신인 경우 (10개 평가마다 갱신) (완벽한 조건)
        if videoRow.prefs and videoRow.ratingVideo_video.count() < videoRow.rated +10:
            successful=True
        else:
            #DB에 값들을 확인하는 참회의 시간을 가져보자.
            if videoRow.ratingVideo_video.count()>4: #평가수가 충분한 경우. 평가수 부족하면 바로 OUT
                if (not videoRow.rated > 4):#평가 수는 충분한데 그 값이 DB에 업데이트되지 않은 경우 or NULL값인경우
                    try: #업데이트 시켜주자
                        videoRow.rated = videoRow.ratingVideo_video.count()
                        db.session.commit()
                    except: pass
                #그럼 이제 .rated는 다 있는거다.
                if not videoRow.prefs:
                    try: #.prefs 값을 넣자
                        itemPrefs = recommendation.simVideoPrefs()
                        list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
                        a = json.dumps(list)
                        videoRow.prefs = a
                        db.session.commit()
                        successful=True
                    except: pass
                try:
                    #값이 최신으로 업데이트 되지 않았을 때
                    if videoRow.ratingVideo_video.count()>=videoRow.rated +10:
                        try:
                            videoRow.rated = videoRow.ratingVideo_video.count()
                            db.session.commit()
                            itemPrefs = recommendation.simVideoPrefs()
                            list = recommendation.getSoulmate(itemPrefs,name,n=5,similarity=recommendation.simPearson)
                            a = json.dumps(list)
                            videoRow.prefs = a
                            db.session.commit()
                            successful=True
                        except: pass
                except:pass
            else: pass #평가수가 부족하니까 OUT
    except:pass
    if successful:
        sList = json.loads(videoRow.prefs)
    

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
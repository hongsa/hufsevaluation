# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, request, flash, session,jsonify
from apps import db
from apps.models import User, Actor, Video, ActorReview, VideoReview,Filmo
from apps import recommendation
import json
import time
import logging
from sqlalchemy import desc
import math
import pytz
import datetime



# def getMicrotime():
#     return time.time()
#
# def timeLogger(message, startTime, endTime):
#     sMessage = message + " :: " + str( endTime - startTime )
#     logging.error( sMessage)

def get_current_time():
    return datetime.datetime.now(pytz.timezone('Asia/Seoul'))


def actorDetail(name):
    # _x = getMicrotime()
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))
    email = session['session_user_email']
    # _s = getMicrotime()
    user = User.query.get(email)
    # _e = getMicrotime()
    # timeLogger(" user", _s, _e)



    # 해당하는 배우추출
    # _s = getMicrotime()
    actorRow = Actor.query.get(name)
    # _e = getMicrotime()
    # timeLogger(" ActorRow", _s, _e)


    #출연작품 가져오기
    # _s = getMicrotime()
    # oFilmo = Filmo.query.filter_by(ActorName=name).all()
    oFilmo = actorRow.filmo_actor
    # _e = getMicrotime()
    # timeLogger(" oFilmo", _s, _e)
    #댓글 가져오기
    # comments = ActorReview.query.filter_by(actorName=name).all()

    # _s = getMicrotime()
    # comments = actorRow.actorReview_actor
    # _e = getMicrotime()
    # timeLogger("comments", _s, _e)
    #유사배우 목록 가져오기
    sList = False
    successful=False



    # _s = getMicrotime()
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

    # _e = getMicrotime()
    # timeLogger("firstTry", _s, _e)

    if successful:
        oList = json.loads(actorRow.prefs)
        sList = []
        for each in oList:
            if each != name:
                sList.append(each)


    # _s = getMicrotime()
    # list = actorRow.actorReview_actor.filter_by(userEmail=email).with_entities(ActorReview.id).all()
    # _e = getMicrotime()
    # timeLogger("list", _s, _e)

    #별점 있는 지 확인
    # rating = actorRow.ratingActor_actor.filter_by(userEmail=email).first()

    # _s = getMicrotime()
    rating = user.ratingActor_user.filter_by(actorName=name).first()
    # _e = getMicrotime()
    # timeLogger("rating", _s, _e)

    # _y = getMicrotime()
    # timeLogger("total", _x, _y)



    if actorRow.category=='1':
        category='진짜 작은애당'
    elif actorRow.category=='2':
        category='품에 쏘오오옥'
    elif actorRow.category =='3':
        category='걸그룹 키당'
    else:
        category='힐 신지 말아조'



    if rating:
        return render_template("actorDetail.html", actorRow=actorRow, oFilmo=oFilmo,rating=rating.rating,sList=sList,category=category)
    else:
        return render_template("actorDetail.html", actorRow=actorRow, oFilmo=oFilmo, sList=sList,category=category)


#댓글입력

def actor_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)
            sUser=user.nickname
            num = user.numVideo
            if num<50:
                sLevel= 0
            elif 50<=num<100:
                sLevel= 1
            elif 100<=num<200:
                sLevel= 2
            elif 200<=num<400:
                sLevel= 3
            else:
                sLevel= 4
            sComment = request.form['comment']
            sName = request.form['actorName']
            thisComment={}
            thisComment=ActorReview(
            actorName=sName,
            userEmail=session['session_user_email'],
            content=sComment,
            created = get_current_time()
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
    # oFilmo = Filmo.query.filter_by(videoName=name).all()
    oFilmo = videoRow.filmo_video
    appearActor = []
    #댓글 가져오기
    # comments = videoRow.reviews()
    # comments = videoRow.videoReview_video
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
        sList = []
        for each in oList:
            if each != name:
                sList.append(each)


    # list = videoRow.videoReview_video.filter_by(userEmail=email).with_entities(VideoReview.id).all()

    if videoRow.category=='1':
        category='러브 액츄얼리'
    elif videoRow.category=='2':
        category='금기된 사랑'
    elif videoRow.category =='3':
        category='코스튬'
    elif videoRow.category =='4':
        category='협동조합'
    elif videoRow.category =='5':
        category='이게 말이 돼?'
    elif videoRow.category =='6':
        category='나 등 밀어줘'


    # rating = videoRow.ratingVideo_video.filter_by(userEmail=email).first()
    rating = user.ratingVideo_user.filter_by(videoName=name).first()
    if rating:
        return render_template("videoDetail.html", videoRow=videoRow, oFilmo=oFilmo,rating=rating.rating,sList=sList,category=category)
    return render_template("videoDetail.html", videoRow=videoRow, oFilmo=oFilmo, sList=sList,category=category)

#댓글입력
def video_comment():
    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)
            sUser=user.nickname
            num = user.numVideo
            if num<50:
                sLevel= 0
            elif 50<=num<100:
                sLevel= 1
            elif 100<=num<200:
                sLevel= 2
            elif 200<=num<400:
                sLevel= 3
            else:
                sLevel= 4
            sComment = request.form['comment']
            sName = request.form['videoName']
            thisComment={}
            thisComment=VideoReview(
            videoName=sName,
            userEmail=session['session_user_email'],
            content=sComment,
            created = get_current_time()
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


def a_comment_rows():

    if request.method == 'POST':
        name = request.form.get('name')
        # num = int(request.form.get('num'))
        actorRow = Actor.query.get(name)
        comments = actorRow.actorReview_actor
        # comments = actorRow.actorReview_actor.order_by(desc(ActorReview.id)).\
        #     offset((num-1)*20).limit(20)

        # total = int(math.ceil(float(actorRow.actorReview_actor.count())/20))

        rows=[]
        # rows.append(total)
        for each in comments:
            if each.user.numVideo<50:
                level= 0
            elif 50<=each.user.numVideo<100:
                level= 1
            elif 100<=each.user.numVideo<200:
                level= 2
            elif 200<=each.user.numVideo<400:
                level= 3
            else:
                level= 4

            rows.append(dict(level=level,user=each.user.nickname,comments=each.content))

        # logging.error(rows)
        return json.dumps(rows)

def v_comment_rows():

    if request.method == 'POST':
        name = request.form.get('name')
        videoRow = Video.query.get(name)
        comments = videoRow.videoReview_video


        rows=[]
        for each in comments:
            if each.user.numVideo<50:
                level= 0
            elif 50<=each.user.numVideo<100:
                level= 1
            elif 100<=each.user.numVideo<200:
                level= 2
            elif 200<=each.user.numVideo<400:
                level= 3
            else:
                level= 4

            rows.append(dict(level=level,user=each.user.nickname,comments=each.content))

        # logging.error(rows)
        return json.dumps(rows)
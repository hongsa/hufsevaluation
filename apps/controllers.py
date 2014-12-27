# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response, \
    current_app, json
from apps import app, db, models
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Actor, Video, ActorReview, VideoReview, Filmo, RatingActor, RatingVideo, Favorite, Bookmark
from sqlalchemy import desc, or_
from apps import forms
import math
from controller import userController

# userController에서 관리하는 부분 시작
@app.route('/')
@app.route('/index')
def index():
    return userController.index()


# 회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return userController.signup()


# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    return userController.login()


#로그아웃 부분.
@app.route('/logout')
def logout():
    return userController.logout()


# 회원 비밀번호 수정
@app.route('/m_pw', methods=['GET', 'POST'])
def modify_password():
    return userController.modify_password()


#회원 닉네임 수정
@app.route('/m_nick', methods=['GET', 'POST'])
def modify_nickname():
    return userController.modify_nickname()


# userController 관리부분 끝



@app.route('/video_main', methods=['GET', 'POST'])
def video_main():
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    totalRank = Video.query.order_by(desc(Video.average)).limit(10)
    categoryOne = Video.query.filter_by(category="1").order_by(desc(Video.average)).limit(5)
    categoryTwo = Video.query.filter_by(category="2").order_by(desc(Video.average)).limit(5)
    categoryThree = Video.query.filter_by(category="3").order_by(desc(Video.average)).limit(5)
    categoryFour = Video.query.filter_by(category="4").order_by(desc(Video.average)).limit(5)
    categoryFive = Video.query.filter_by(category="5").order_by(desc(Video.average)).limit(5)
    categorySix = Video.query.filter_by(category="6").order_by(desc(Video.average)).limit(5)

    return render_template("video_main.html", totalRank=totalRank, categoryOne=categoryOne, categoryTwo=categoryTwo,
                           categoryThree=categoryThree, categoryFour=categoryFour, categoryFive=categoryFive,
                           categorySix=categorySix)


@app.route('/show1/<key>', methods=['GET', 'POST'])
def show1(key):
    video = Video.query.get(key)
    mimetype = "image/png"
    return current_app.response_class(video.image, mimetype=mimetype)


@app.route('/actor_main', methods=['GET', 'POST'])
def actor_main():
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    totalRank = Actor.query.order_by(desc(Actor.average)).limit(10)
    categoryOne = Actor.query.filter_by(category="1").order_by(desc(Actor.average)).limit(5)
    categoryTwo = Actor.query.filter_by(category="2").order_by(desc(Actor.average)).limit(5)
    categoryThree = Actor.query.filter_by(category="3").order_by(desc(Actor.average)).limit(5)
    # categoryFour = Actor.query.filter_by(category="4").order_by(desc(Actor.average)).limit(5)
    # categoryFive = Actor.query.filter_by(category="5").order_by(desc(Actor.average)).limit(5)
    # categorySix = Actor.query.filter_by(category="6").order_by(desc(Actor.average)).limit(5)

    return render_template("actor_main.html", totalRank=totalRank, categoryOne=categoryOne, categoryTwo=categoryTwo,
                           categoryThree=categoryThree)


@app.route('/show2/<key>', methods=['GET', 'POST'])
def show2(key):
    actor = Actor.query.get(key)
    mimetype = "image/png"
    return current_app.response_class(actor.image, mimetype=mimetype)


@app.route('/a_category/<path:name>', defaults={'page': 1})
@app.route('/a_category/<path:name>/<int:page>', methods=['GET', 'POST'])
def actor_category(name, page):
    actorCategory = Actor.query.filter_by(category=name).order_by(desc(Actor.average)).offset(
        (page - 1) * 12).limit(12)
    total = Actor.query.filter_by(category=name).count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    category = Actor.query.filter_by(category=name).first().category

    return render_template("actor_category.html", actorCategory=actorCategory, category=category,
                           total_page=range(1, int(total_page + 1)))


@app.route('/v_category/<path:name>', defaults={'page': 1})
@app.route('/v_category/<path:name>/<int:page>', methods=['GET', 'POST'])
def video_category(name, page):
    videoCategory = Video.query.filter_by(category=name).order_by(desc(Video.average)).offset(
        (page - 1) * 12).limit(12)
    total = Video.query.filter_by(category=name).count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    category = Video.query.filter_by(category=name).first().release

    return render_template("video_category.html", videoCategory=videoCategory, category=category,
                           total_page=range(1, int(total_page + 1)))


@app.route('/n_actor/<int:name>', defaults={'page': 1})
@app.route('/n_actor/<int:name>/<int:page>', methods=['GET', 'POST'])
def new_actor(name, page):
    releaseList = set([int(each.release) for each in Actor.query.all()])
    logging.error(releaseList)
    actorRelease = Actor.query.filter(Actor.release * 100 > name * 100,
                                      Actor.release * 100 < (name + 1) * 100).order_by(desc(Actor.release)).offset(
        (page - 1) * 12).limit(12)
    logging.error(actorRelease)
    total = Actor.query.filter(Actor.release * 100 > name * 100, Actor.release * 100 < (name + 1) * 100).count()
    logging.error(total)
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    release = int(
        Actor.query.filter(Actor.release * 100 > name * 100, Actor.release * 100 < (name + 1) * 100).first().release)

    return render_template("new_actor_main.html", releaseList=releaseList, actorRelease=actorRelease, release=release,
                           total_page=range(1, int(total_page + 1)))


@app.route('/n_video/<path:name>', defaults={'page': 1})
@app.route('/n_video/<path:name>/<int:page>', methods=['GET', 'POST'])
def new_video(name, page):
    companyList = set([each.company for each in Video.query.all()])
    videoCompany = Video.query.filter_by(company=name).order_by(desc(Video.release)).offset(
        (page - 1) * 12).limit(12)
    total = Video.query.filter_by(company=name).count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    company = Video.query.filter_by(company=name).first().company

    return render_template("new_video_main.html", companyList=companyList, videoCompany=videoCompany, company=company,
                           total_page=range(1, int(total_page + 1)))


import logging
#디비검색
@app.route('/db_search', methods=['GET', 'POST'])
def db_search(searching_word):
    video_list = Video.query.all()
    actor_list = Actor.query.all()
    selected_video = []
    selected_actor = []
    if searching_word != "":
        for i in video_list:
            if (i.name.lower()).find(searching_word.lower()) != -1:
                selected_video.append(i.name)
                logging.error(selected_video)
        try:
            selected_video[0]
        except Exception, e:

            for j in actor_list:
                if (j.name).find(searching_word) != -1:
                    selected_actor.append(j.name)
            try:
                selected_actor[0]
            except Exception, e:

                selected_actor.append(u"검색결과가 없습니다.ㅠㅜ")

        return render_template("search_result.html", selected_video=selected_video, selected_actor=selected_actor,
                               searching_word=searching_word)

    selected_actor.append(u"검색어를 입력해주세요!")
    return render_template("search_result.html", selected_video=selected_video, selected_actor=selected_actor,
                           searching_word=searching_word)


#구글검색
@app.route('/g_search', methods=['GET', 'POST'])
def g_search():
    a = request.args['submitbutton']
    if a == u'first':

        command = request.args['search']
        b = db_search(command)
        return b
    elif a == u'second':
        basicurl = "https://www.google.co.kr/search?q="
        url = basicurl + request.args['search'] + ' ' + 'torrent'
        return redirect(url)

    return "g_search"


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        return render_template("admin.html")

    return redirect(url_for("index"))


@app.route('/admin_actor', methods=['GET', 'POST'])
def admin_actor():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:

        if request.method == 'POST':
            files = request.files['actor_image']
            filestream = files.read()

            actor_write = Actor(
                name=request.form['name'],
                image=filestream,
                category=request.form['category'],
                age=request.form['age'],
                release=request.form['release']
            )
            db.session.add(actor_write)
            db.session.commit()
            flash(u"배우 DB에 저장되었습니다.")
            return redirect(url_for("admin"))

        return render_template("admin.html")

    return redirect(url_for("index"))


@app.route('/admin_actor_check', methods=['GET', 'POST'])
def admin_actor_check():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            name = request.form['name']
            actor = Actor.query.get(name)
            if actor:
                flash(u"이미 있는 배우입니다.")
                return redirect(url_for("admin"))
            else:
                flash(u"없는 배우입니다.")
                return redirect(url_for("admin"))

    return redirect(url_for("index"))


@app.route('/admin_video', methods=['GET', 'POST'])
def admin_video():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            files = request.files['video_image']
            filestream = files.read()

            video_write = Video(
                name=request.form['name'],
                image=filestream,
                category=request.form['category'],
                company=request.form['company'],
                release=request.form['release'],
                exposure=request.form['exposure']
            )
            db.session.add(video_write)
            db.session.commit()

            flash(u"영상 DB에 저장되었습니다.")
            return redirect(url_for("admin"))

        return render_template("admin.html")

    return redirect(url_for("index"))


@app.route('/admin_connect', methods=['GET', 'POST'])
def admin_connect():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            connect = Filmo(
                ActorName=request.form['actor_name'],
                videoName=request.form['video_name']
            )
            db.session.add(connect)
            db.session.commit()
            flash(u"잘 연결되었습니다.")

            return redirect(url_for("admin"))

        return render_template("admin.html")

    return redirect(url_for("index"))


@app.route('/a_collection_b/<int:page>', defaults={'page': 1})
@app.route('/a_collection_b/<int:page>', methods=['GET', 'POST'])
def actor_collection_bookmark(page):
    email = session['session_user_email']
    user = User.query.get(email)
    myBookmark = user.favorite_user.offset((page - 1) * 12).limit(12)
    total = user.favorite_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("actor_collection_bookmark.html", myBookmark=myBookmark,
                           total_page=range(1, int(total_page + 1)))


@app.route('/a_collection_r/<int:page>', defaults={'page': 1})
@app.route('/a_collection_r/<int:page>', methods=['GET', 'POST'])
def actor_collection_rating(page):
    email = session['session_user_email']
    user = User.query.get(email)
    myRating = user.ratingActor_user.order_by(RatingActor.rating.desc()).offset((page - 1) * 12).limit(12)
    total = user.ratingActor_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("actor_collection_rating.html", myRating=myRating, total_page=range(1, int(total_page + 1)))


@app.route('/v_collection_b/<int:page>', defaults={'page': 1})
@app.route('/v_collection_b/<int:page>', methods=['GET', 'POST'])
def video_collection_bookmark(page):
    email = session['session_user_email']
    user = User.query.get(email)
    myBookmark = user.bookmark_user.offset((page - 1) * 12).limit(12)
    total = user.bookmark_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("video_collection_bookmark.html", myBookmark=myBookmark,
                           total_page=range(1, int(total_page + 1)))


@app.route('/v_collection_r/<int:page>', defaults={'page': 1})
@app.route('/v_collection_r/<int:page>', methods=['GET', 'POST'])
def video_collection_rating(page):
    email = session['session_user_email']
    user = User.query.get(email)
    myRating = user.ratingVideo_user.order_by(RatingVideo.rating.desc()).offset((page - 1) * 12).limit(12)
    total = user.ratingVideo_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("video_collection_rating.html", myRating=myRating, total_page=range(1, int(total_page + 1)))


import logging


@app.route('/v_save_star', methods=['GET', 'POST'])
def video_save_star():
    star = int(request.form.get('star'))
    logging.error(star)
    name = request.form.get('name')
    logging.error(name)
    video = Video.query.get(name)
    logging.error(video)
    email = session['session_user_email']
    logging.error(email)

    rating = video.ratingVideo_video.filter_by(userEmail=email).first()
    logging.error(rating)

    if rating:  # 이미 평점을 매겼었음
        video.score += star - rating.rating
        a = float(video.score / video.count)
        video.average = float(math.ceil(a * 100) / 100)
        rating.rating = star

    else:  # 평점을 매긴 적이 없음
        rating = RatingVideo(
            videoName=video.name,
            userEmail=email,
            rating=star)

        video.count += 1
        video.score += star
        a = float(video.score / video.count)
        video.average = float(math.ceil(a * 100) / 100)

    db.session.add(rating)
    db.session.commit()

    return jsonify(success=True)


import logging


@app.route('/a_save_star', methods=['GET', 'POST'])
def actor_save_star():
    star = int(request.form.get('star'))
    logging.error(star)
    name = request.form.get('name')
    logging.error(name)
    actor = Actor.query.get(name)
    logging.error(actor)
    email = session['session_user_email']
    logging.error(email)

    rating = actor.ratingActor_actor.filter_by(userEmail=email).first()

    if rating:  # 이미 평점을 매겼었음
        actor.score += star - rating.rating
        a = float(actor.score / actor.count)
        actor.average = float(math.ceil(a * 100) / 100)
        rating.rating = star

    else:  # 평점을 매긴 적이 없음
        rating = RatingActor(
            actorName=actor.name,
            userEmail=email,
            rating=star)

        actor.count += 1
        actor.score += star
        a = float(actor.score / actor.count)
        actor.average = float(math.ceil(a * 100) / 100)

    db.session.add(rating)
    db.session.commit()

    return jsonify(success=True)


@app.route('/a_bookmark', methods=['GET', 'POST'])
def actor_bookmark():
    name = request.form.get('name')
    logging.error(name)
    actor = Actor.query.get(name)
    logging.error(actor)
    email = session['session_user_email']
    logging.error(email)
    bookmark = actor.favorite_actor.filter_by(userEmail=email).first()
    logging.error(email)

    if bookmark:
        return jsonify(success=True)

    my_bookmark = Favorite(
        actorName=name,
        userEmail=email
    )
    db.session.add(my_bookmark)
    db.session.commit()

    return jsonify(success=True)


@app.route('/v_bookmark', methods=['GET', 'POST'])
def video_bookmark():
    name = request.form.get('name')
    logging.error(name)
    video = Video.query.get(name)
    logging.error(video)
    email = session['session_user_email']
    logging.error(email)
    bookmark = video.bookmark_video.filter_by(userEmail=email).first()
    logging.error(email)

    if bookmark:
        return jsonify(success=True)

    my_bookmark = Bookmark(
        videoName=name,
        userEmail=email
    )
    db.session.add(my_bookmark)
    db.session.commit()

    return jsonify(success=True)


# 배우 디테일
@app.route('/actorDetail/<string:name>', methods=['GET', 'POST'])
def actorDetail(name):
    # 해당하는 배우추출
    actorRow = Actor.query.get(name)

    #출연작품 가져오기
    appearVideo = actorRow.videos()
    #댓글 가져오기
    comments = actorRow.reviews()

    return render_template("actorDetail.html", actorRow=actorRow, appearVideo=appearVideo, comments=comments)


#댓글입력

@app.route('/actor/comment', methods=['POST'])
def actor_comment():
    try:
        if request.method == 'POST':
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
            jsonDict['comments'] = sComment
            jsonDict['actorName'] = sName
            logging.error(json.dumps(jsonDict))
            db.session.add(thisComment)
            db.session.commit()

            return json.dumps(jsonDict)

    except Exception, e:
        print " Occuring Exception. ", e


@app.route('/videoDetail/<string:name>', methods=['GET', 'POST'])
def videoDetail(name):
    # 해당하는 배우추출
    videoRow = Video.query.get(name)

    #출연작품 가져오기
    appearActor = videoRow.actors()
    #댓글 가져오기
    comments = videoRow.reviews()

    return render_template("videoDetail.html", videoRow=videoRow, appearActor=appearActor, comments=comments)


#댓글입력

@app.route('/video/comment', methods=['POST'])
def video_comment():
    try:
        sComment = request.form['comment']
        sName = request.form['actorName']

        #댓글 DB에 저장
        if request.method == 'POST':
            # if not 'session_user_email' in session:
            #     return redirect(url_for("login"))
            #
            # thisComment=ActorReview(
            # actorName=sName,
            # userEmail=session['session_user_email'],
            # content=request.form['content']
            # )
            #
            # db.session.add(thisComment)
            # db.session.commit()

            # Create JSON String
            jsonDict = {}
            jsonDict['comments'] = sComment
            jsonDict['actorName'] = sName
            logging.error(jsonDict)
            return jsonify(success=True, result=jsonDict)

    except Exception, e:
        print " Occuring Exception. ", e


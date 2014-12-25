# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response, \
    current_app
from apps import app, db, models
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Actor, Video, ActorReview, VideoReview, Filmo, RatingActor, RatingVideo, Favorite, Bookmark
from sqlalchemy import desc
from apps import forms
import math
import json

@app.route('/')
@app.route('/index')
def index():
    if not 'session_user_email' in session:
        form=forms.JoinForm()
        form2=forms.LoginForm()
        session['if_confirm'] = "true"
        return render_template("main_page.html", form=form,form2=form2)
    return redirect(url_for('actor_main'))


# 회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    form = forms.JoinForm()
    form2 = forms.LoginForm()

    try:
        if session['session_user_email']:
            flash(u"이미 회원가입 하셨습니다!", "error")
            return render_template("main_page.html", form=form, form2=form2)
    except Exception, e:
        pass

    if request.method == 'POST':
        if User.query.get(form.email.data):
            session.clear()
            flash(u"이미 등록된 메일 주소 입니다!", "error")
            return render_template("main_page.html", form=form, form2=form2)
        if User.query.get(form.nickname.data):
            session.clear()
            flash(u"이미 사용중인 닉네임입니다!", "error")
            return render_template("main_page.html", form=form, form2=form2)
        if not form.validate_on_submit():
            session.clear()
            flash(u"올바른 형식으로 입력해주세요!", "error")
            return render_template("main_page.html", form=form, form2=form2)

        user = User(email=form.email.data, password=generate_password_hash(form.password.data),
                    nickname=form.nickname.data, sex=form.sex.data)

        db.session.add(user)
        db.session.commit()

        session.clear()

        # flash(u"회원가입 되셨습니다!")
        session['session_user_email'] = form.email.data
        session['session_user_nickname'] = form.nickname.data

        return redirect(url_for('actor_main'))

    session.clear()
    flash(u"잘못 입력하셨습니다!","error")
    return render_template("main_page.html", form=form, form2=form2)



#로그인
@app.route('/login', methods=['GET', 'POST'])
def login():

    form = forms.JoinForm()
    form2 = forms.LoginForm()

    try:
        if session['session_user_email']:
            flash(u'이미 로그인 하셨습니다!', "error")
            return redirect(url_for('actor_main'))

    except Exception, e:
        pass


    if request.method == "POST":
        if form2.validate_on_submit():
            email = form.email.data
            pwd = form.password.data
            user = User.query.get(email)
            if user is None:
                session.clear()
                flash(u"존재하지 않는 이메일 입니다.", "error")
                return render_template("main_page.html", form=form, form2=form2)
            elif not check_password_hash(user.password, pwd):
                session.clear()
                flash(u"비밀번호가 일치하지 않습니다.", "error")
                return render_template("main_page.html", form=form, form2=form2)
            else:
                session.permanent = True
                session['session_user_email'] = user.email
                session['session_user_nickname'] = user.nickname
                return redirect(url_for('actor_main'))


    session.clear()

    flash(u"잘못 입력하셨습니다!","error")

    return render_template("main_page.html", form=form, form2=form2)

#로그아웃 부분.
@app.route('/logout')
def logout():

    if "session_user_email" in session:
        session.clear()
        # flash(u"로그아웃 되었습니다.")
    else:
        flash(u"로그인 되어있지 않습니다.", "error")
    return redirect(url_for('index'))

@app.route('/m_pw', methods=['GET', 'POST'])
def modify_password():
    if request.method == 'POST':
        email = session['session_user_email']
        user= User.query.get(email)
        user.password = generate_password_hash(request.form['password'])
        db.session.commit()
        flash(u"변경 완료되었습니다.", "password")
        return redirect(url_for('modify_password'))

    return render_template("modify.html")

@app.route('/m_nick', methods=['GET', 'POST'])
def modify_nickname():
    if request.method == 'POST':
        email = session['session_user_email']
        user= User.query.get(email)

        nickname=request.form['nickname']
        nickname_list=[]
        for i in User.query.all():
		    nickname_list.append(i.nickname)
        if nickname in nickname_list:
            flash(u"이미 사용 중인 닉네임 입니다.", "nickname")
            return redirect(url_for('modify_nickname'))

        user.nickname=nickname
        db.session.commit()
        session['session_user_nickname'] = user.nickname
        flash(u"변경 완료되었습니다.", "nickname")
        return redirect(url_for('modify_nickname'))

    return render_template("modify.html")


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
    categoryFour = Actor.query.filter_by(category="4").order_by(desc(Actor.average)).limit(5)
    categoryFive = Actor.query.filter_by(category="5").order_by(desc(Actor.average)).limit(5)
    categorySix = Actor.query.filter_by(category="6").order_by(desc(Actor.average)).limit(5)

    return render_template("actor_main.html", totalRank=totalRank, categoryOne=categoryOne, categoryTwo=categoryTwo,
                           categoryThree=categoryThree, categoryFour=categoryFour, categoryFive=categoryFive,
                           categorySix=categorySix)


@app.route('/show2/<key>', methods=['GET', 'POST'])
def show2(key):
    actor = Actor.query.get(key)
    mimetype = "image/png"
    return current_app.response_class(actor.image, mimetype=mimetype)


@app.route('/a_category/<path:name>',defaults={'page': 1})
@app.route('/a_category/<path:name>/<int:page>',methods=['GET','POST'])
def actor_category(name,page):

    actorCategory = Actor.query.filter_by(category=name).order_by(desc(Actor.average)).offset(
        (page - 1) * 12).limit(12)
    total = Actor.query.filter_by(category=name).count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    category = Actor.query.first().category

    return render_template("actor_category.html", actorCategory=actorCategory, category=category, total_page=range(1, int(total_page + 1)))


@app.route('/v_category/<path:name>',defaults={'page': 1})
@app.route('/v_category/<path:name>/<int:page>',methods=['GET','POST'])
def video_category(name,page):

    videoCategory = Video.query.filter_by(category=name).order_by(desc(Video.average)).offset(
        (page - 1) * 12).limit(12)
    total = Video.query.filter_by(category=name).count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    category = Video.query.first().category

    return render_template("video_category.html",videoCategory=videoCategory, category=category, total_page=range(1, int(total_page + 1)))


@app.route('/n_actor/<path:name>',defaults={'page': 1})
@app.route('/n_actor/<path:name>/<int:page>',methods=['GET','POST'])
def new_actor(name,page):

    companyList = set([each.company for each in Actor.query.all()])
    actorCompany = Actor.query.filter_by(company=name).order_by(desc(Actor.release)).offset(
        (page - 1) * 12).limit(12)
    total = Actor.query.filter_by(company=name).count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    company = Actor.query.first().company

    return render_template("new_actor_main.html", companyList=companyList,actorCompany=actorCompany, company=company, total_page=range(1, int(total_page + 1)))

@app.route('/n_video/<path:name>',defaults={'page': 1})
@app.route('/n_video/<path:name>/<int:page>',methods=['GET','POST'])
def new_video(name,page):

    companyList = set([each.company for each in Video.query.all()])
    videoCompany = Video.query.filter_by(company=name).order_by(desc(Video.release)).offset(
        (page - 1) * 12).limit(12)
    total = Video.query.filter_by(company=name).count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    company = Video.query.first().company

    return render_template("new_video_main.html", companyList=companyList,videoCompany=videoCompany, company=company, total_page=range(1, int(total_page + 1)))


import logging
#디비검색
@app.route('/db_search', methods=['GET', 'POST'])
def db_search(searching_word):

    video_list = Video.query.all()
    actor_list = Actor.query.all()
    selected = []
    if searching_word != "":
        for i in video_list:
            if (i.name.lower()).find(searching_word.lower()) != -1:
                selected.append(i.name)
                logging.error(selected)
        try:
            selected[0]
        except Exception, e:

            for j in actor_list:
                if (j.name).find(searching_word) != -1:
                    selected.append(j.name)
            try:
                selected[0]
            except Exception, e:
                selected.append(u"검색결과가 없습니다.ㅠㅜ")
        return render_template("search_result.html", selected=selected, searching_word=searching_word)

    selected.append(u"검색어를 입력해주세요!")
    return render_template("search_result.html", selected=selected, searching_word=searching_word)


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
    if session['session_user_email']=='ydproject777@gmail.com':
        return render_template("admin.html")

    return redirect(url_for("index"))



@app.route('/admin_actor', methods=['GET', 'POST'])
def admin_actor():
    if session['session_user_email']=='ydproject777@gmail.com':
        if request.method == 'POST':
            files = request.files['actor_image']
            filestream = files.read()

            actor_write = Actor(
                name=request.form['name'],
                image=filestream,
                category=request.form['category'],
                company=request.form['company'],
                release=request.form['release']
            )
            db.session.add(actor_write)
            db.session.commit()
            flash(u"배우 DB에 저장되었습니다.")
            return redirect(url_for("admin"))

        return render_template("admin.html")

    return redirect(url_for("index"))


@app.route('/admin_video', methods=['GET', 'POST'])
def admin_video():
    if session['session_user_email']=='ydproject777@gmail.com':
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
    if session['session_user_email']=='ydproject777@gmail.com':
        if request.method == 'POST':

            connect= Filmo(
            ActorName=request.form['actor_name'],
            videoName=request.form['video_name']
            )
            db.session.add(connect)
            db.session.commit()
            flash(u"잘 연결되었습니다.")

            return redirect(url_for("admin"))

        return render_template("admin.html")

    return redirect(url_for("index"))


@app.route('/a_collection_b/<int:page>',defaults={'page': 1})
@app.route('/a_collection_b/<int:page>', methods=['GET', 'POST'])
def actor_collection_bookmark(page):

    email = session['session_user_email']
    user=User.query.get(email)
    myBookmark = user.favorite_user.offset((page - 1) * 12).limit(12)
    total = user.favorite_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("actor_collection_bookmark.html",myBookmark=myBookmark,total_page=range(1, int(total_page + 1)))

@app.route('/a_collection_r/<int:page>',defaults={'page': 1})
@app.route('/a_collection_r/<int:page>', methods=['GET', 'POST'])
def actor_collection_rating(page):

    email = session['session_user_email']
    user=User.query.get(email)
    myRating = user.ratingActor_user.order_by(RatingActor.rating.desc()).offset((page - 1) * 12).limit(12)
    total = user.ratingActor_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("actor_collection_rating.html",myRating=myRating,total_page=range(1, int(total_page + 1)))

@app.route('/v_collection_b/<int:page>',defaults={'page': 1})
@app.route('/v_collection_b/<int:page>', methods=['GET', 'POST'])
def video_collection_bookmark(page):

    email = session['session_user_email']
    user=User.query.get(email)
    myBookmark = user.bookmark_user.offset((page - 1) * 12).limit(12)
    total = user.bookmark_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("video_collection_bookmark.html",myBookmark=myBookmark,total_page=range(1, int(total_page + 1)))

@app.route('/v_collection_r/<int:page>',defaults={'page': 1})
@app.route('/v_collection_r/<int:page>', methods=['GET', 'POST'])
def video_collection_rating(page):

    email = session['session_user_email']
    user=User.query.get(email)
    myRating = user.ratingVideo_user.order_by(RatingVideo.rating.desc()).offset((page - 1) * 12).limit(12)
    total = user.ratingVideo_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    return render_template("video_collection_rating.html",myRating=myRating,total_page=range(1, int(total_page + 1)))



import logging
@app.route('/v_save_star', methods=['GET','POST'])
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
@app.route('/a_save_star', methods=['GET','POST'])
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

@app.route('/a_bookmark',methods=['GET','POST'])
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

    my_bookmark=Favorite(
		actorName=name,
		userEmail=email
		)
    db.session.add(my_bookmark)
    db.session.commit()

    return jsonify(success=True)

@app.route('/v_bookmark',methods=['GET','POST'])
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

    my_bookmark=Bookmark(
		videoName=name,
		userEmail=email
		)
    db.session.add(my_bookmark)
    db.session.commit()

    return jsonify(success=True)


# 배우 디테일
@app.route('/actorDetail/<string:name>',methods=['GET','POST'])
def actorDetail(name):
# 해당하는 배우추출
    actorRow = Actor.query.get(name)
# 배우이름
    actorName = actorRow.name

#출연작품 가져오기
    appearVideo=actorRow.videos()
#댓글 가져오기
    comments=actorRow.reviews()

    average = float(actorRow.average)
    average = float("{0:.2f}".format(average))


    logging.error(appearVideo)
    logging.error(comments)



    return render_template("actorDetail.html", actorName=actorName, appearVideo=appearVideo, comments=comments, average=average, )


#댓글입력

@app.route('/actor/comment', methods=['POST'] )
def comment():

    try:
        sComment = request.form['comment']
        sName = request.form['actorName']

#댓글 입력부분
        if request.method=='POST':
            if not 'session_user_email' in session:
                return redirect(url_for("login"))

            thisComment=ActorReview(
            actorName=sName,
            userEmail=session['session_user_email'],
            content=request.form['content']
            )

            db.session.add(thisComment)
            db.session.commit()

            # Create JSON String
            jsonDict = {}
            jsonDict['comments'] = sComment
            # jsonDict['actorName'] = sName
            logging.error(jsonDict)
            return jsonify(success=True,result=jsonDict)

    except Exception, e:
        print " Occuring Exception. " , e



# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response,current_app
from apps import app,db, models
from werkzeug.security import generate_password_hash, check_password_hash
from models import User,Actor,Video,ActorReview,VideoReview,Filmo,Rating,Favorite,Bookmark

from sqlalchemy import desc
from apps import forms

@app.route('/')

@app.route('/index')
def index():
    form = forms.JoinForm()
    form2 = forms.LoginForm()
    return render_template("main_page.html",form=form,form2=form2)

#회원가입
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    try:
        if session['session_user_email']:
            flash(u"이미 회원가입 하셨습니다!","error")
            return redirect(url_for('index'))
    except Exception, e:
        pass
    form = forms.JoinForm()
    form2 = forms.LoginForm()

    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(u"올바른 형식으로 입력해주세요!","error")
            return render_template("main_page.html",form=form,form2=form2)
        if User.query.get(form.email.data):
            flash(u"이미 등록된 메일 주소 입니다!","error")
            return render_template("main_page.html",form=form,form2=form2)
        if User.query.get(form.nickname.data):
            flash(u"이미 사용중인 닉네임입니다!","error")
            return render_template("main_page.html",form=form,form2=form2)
        user = User(email=form.email.data, password=generate_password_hash(form.password.data), nickname=form.nickname.data)
        db.session.add(user)
        db.session.commit()
        flash(u"회원가입 되셨습니다!")
        session['session_user_email'] = form.email.data
        session['session_user_nickname'] = form.nickname.data 

        return redirect(url_for('actor_main'))



    return redirect(url_for('index'))

#로그인
@app.route('/login', methods = ['GET', 'POST'])
def login():
    try:
        if session['session_user_email']:
            flash(u'이미 로그인 하셨습니다!')
            return redirect(url_for('actor_main'))

    except Exception, e:
        pass
    form = forms.JoinForm()
    form2 = forms.LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            pwd = form.password.data
            user = User.query.get(email)
            if user is None:
                flash(u"존재하지 않는 이메일 입니다.", "error")
            elif not check_password_hash(user.password, pwd):
                flash(u"비밀번호가 일치하지 않습니다.", "error")
            else:
                session.permanent = True
                session['session_user_id'] = user.id
                session['session_user_nickname'] = user.nickname
                return redirect(url_for('actor_main'))
    return redirect(url_for('index'))

#로그아웃 부분.
@app.route('/logout')
def logout():
    if "session_user_id" in session:
        session.clear()
        flash(u"로그아웃 되었습니다.")
    else:
        flash(u"로그인 되어있지 않습니다.", "error")
    return redirect(url_for('index'))


@app.route('/video_main')
def video_main():

    totalRank = Video.query.order_by(desc(Video.average)).limit(10)
    categoryOne =Video.query.filter_by(category="1").order_by(desc(Video.average)).limit(5)
    categoryTwo =Video.query.filter_by(category="2").order_by(desc(Video.average)).limit(5)
    categoryThree =Video.query.filter_by(category="3").order_by(desc(Video.average)).limit(5)
    categoryFour =Video.query.filter_by(category="4").order_by(desc(Video.average)).limit(5)
    categoryFive =Video.query.filter_by(category="5").order_by(desc(Video.average)).limit(5)
    categorySix =Video.query.filter_by(category="6").order_by(desc(Video.average)).limit(5)

    return render_template("video_main.html", totalRank=totalRank, categoryOne=categoryOne, categoryTwo=categoryTwo,categoryThree=categoryThree,categoryFour=categoryFour, categoryFive=categoryFive, categorySix=categorySix)


@app.route('/show1/<key>', methods=['GET','POST'])
def show1(key):
    video = Video.query.get(key)
    mimetype ="image/png"
    return current_app.response_class(video.image, mimetype = mimetype)

@app.route('/actor_main')
def actor_main():

    totalRank = Actor.query.order_by(desc(Actor.average)).limit(10)
    categoryOne =Actor.query.filter_by(category="1").order_by(desc(Actor.average)).limit(5)
    categoryTwo =Actor.query.filter_by(category="2").order_by(desc(Actor.average)).limit(5)
    categoryThree =Actor.query.filter_by(category="3").order_by(desc(Actor.average)).limit(5)
    categoryFour =Actor.query.filter_by(category="4").order_by(desc(Actor.average)).limit(5)
    categoryFive =Actor.query.filter_by(category="5").order_by(desc(Actor.average)).limit(5)
    categorySix =Actor.query.filter_by(category="6").order_by(desc(Actor.average)).limit(5)

    return render_template("actor_main.html",totalRank=totalRank, categoryOne=categoryOne, categoryTwo=categoryTwo,categoryThree=categoryThree,categoryFour=categoryFour, categoryFive=categoryFive, categorySix=categorySix)

@app.route('/show2/<key>', methods=['GET','POST'])
def show2(key):
    actor = Actor.query.get(key)
    mimetype ="image/png"
    return current_app.response_class(actor.image, mimetype = mimetype)

@app.route('/a_category/<path:name>')
def actor_category(name):
    actorCategory = Actor.query.filter_by(category=name)
    categoryList = set([each.category for each in Actor.query.all()])

    return render_template("actor_category.html",actorCategory=actorCategory, categoryList=categoryList, name=name)

@app.route('/v_category/<path:name>')
def video_category(name):
    videoCategory = Video.query.filter_by(category=name)
    categoryList = set([each.category for each in Video.query.all()])

    return render_template("video_category.html",videoCategory=videoCategory, categoryList=categoryList, name=name)



@app.route('/new_video_main')
def new_video_main():
	return render_template("new_video_main.html")


#디비검색
@app.route('/db_search', methods=['GET', 'POST'])
def db_search(searching_word):
	video_list = models.Video.query.all()
	actor_list = models.Actor.query.all()
	selected=[]
	if searching_word != "":
		for i in video_list:
			if (i.name.lower()).find(searching_word.lower()) != -1:
					selected.append(i.name)
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
	if a==u'first':

		command = request.args['search']
		b = db_search(command)
		return b
	elif a==u'second':
		basicurl = "https://www.google.co.kr/search?q="
		url = basicurl + request.args['search'] + ' ' + 'torrent'
		return redirect(url)

	return "g_search"


@app.route('/admin', methods=['GET','POST'])
def admin():
	# if session['session_user_email']=='ydproject777@gmail.com':
    return render_template("admin.html")

	# return redirect(url_for("index"))



@app.route('/admin_actor',methods=['GET','POST'])
def admin_actor():
	# if session['session_user_email']=='ydproject777@gmail.com':
    if request.method=='POST':
        files = request.files['actor_image']
        filestream = files.read()

        actor_write=Actor(
            name=request.form['name'],
            image = filestream,
            category=request.form['category']
            )
        db.session.add(actor_write)
        db.session.commit()
        flash(u"배우 DB에 저장되었습니다.")
        return redirect(url_for("admin"))
    return render_template("admin.html")
	# return redirect(url_for("index"))


@app.route('/admin_video',methods=['GET','POST'])
def admin_video():
	# if session['session_user_email']=='ydproject777@gmail.com':
    if request.method=='POST':
        files = request.files['video_image']
        filestream = files.read()

        video_write=Video(
            name=request.form['name'],
            image = filestream,
            category=request.form['category'],
            release=request.form['release_year'],
            exposure=request.form['exposure'],
            )
        db.session.add(video_write)
        db.session.commit()
        flash(u"영상 DB에 저장되었습니다.")
        return redirect(url_for("admin"))
    return render_template("admin.html")
	# return redirect(url_for("index"))






















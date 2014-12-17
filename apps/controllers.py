# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response,current_app
from apps import app,db, models
from werkzeug.security import generate_password_hash, check_password_hash
from models import User,Actor,Video,ActorReview,VideoReview,Filmo,Rating,Favorite,Bookmark

from sqlalchemy import desc

@app.route('/')

@app.route('/index')
def index():
    return render_template("main_page.html")

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
	video = Actor.query.get(key)
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
    content={}
    content['actorCategory'] = Actor.query.filter_by(category='name')
    return render_template("actor_category.html",content=content, name=name)

@app.route('/v_category/<path:name>')
def video_category(name):
    content={}
    content['videoCategory'] = Video.query.filter_by(category='name')
    return render_template("video_category.html",content=content, name=name)

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

























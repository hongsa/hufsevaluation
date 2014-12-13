# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response,current_app
from apps import app,db, models
from werkzeug.security import generate_password_hash, check_password_hash
from models import Actor,Video,User,Actor_review,Video_review,Actor_Video,Rating,Bookmark

from sqlalchemy import desc

@app.route('/')

@app.route('/index')
def index():
    return render_template("main_page.html")

@app.route('/category')
def category_main():
	return render_template("category_layout.html")

@app.route('/video_main')
def video_main():
	return render_template("video_main.html")

@app.route('/actress_main')
def actress_main():
	return render_template("actress_main.html")

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
				selected.append(u"해당하는 검색결과가 없습니다.ㅠㅜ")
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

























# -*- coding:utf-8 -*-
from sqlalchemy import desc

__author__ = 'bebop'

from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response,current_app
from werkzeug.security import generate_password_hash, check_password_hash
from apps import app,db
from apps.core.model.models import Actor, Filmo, Rating, Bookmark
from apps.core.model import models as models


def actress_main():
	view_row={}
	view_row = models.Actor.query.order_by(desc(models.Actor.score)).limit(9)

	content={}
	content['category_list'] = set([each.category for each in models.Actor.query.all()])


	return render_template("actress_main.html", view_row=view_row, content=content)


def actress_detail(id):
	# review_id=name
	actressDetail = models.Actor.query.get(id)

	#사진 가져오기
	actorImage = url_for("show1", key = id)
	appearVideo={}
	appearVideo =actressDetail.filmo.all()

	review=actressDetail.actorReview.all()

	if request.method=='POST':
		if not 'session_user_email' in session:
			return redirect(url_for("login"))
		
		currentReview=models.ActorReview(
		actorID=id,
		userID=session['session_user_id'],
		content=request.form['content']
		)
		db.session.add(currentReview)
		db.session.commit()
		return redirect(url_for("actress_detail", id = id))

	average = float(actressDetail.score)/actressDetail.count

	average = float("{0:.2f}".format(average))

	return render_template("actress_detail.html", actressDetail=actressDetail, appearVideo=appearVideo, review=review, actorImage = actorImage, average=average, )



#배우 카테고리

def categorize_actor(name):
	content = {}
	content['actor_f_list'] = models.Actor.query.filter_by(category=name)
	# content['video_f_list'] = Video.query.order_by(desc(Video.date_created)).filter_by(category=name)
	# content['actor_list'] = Actor.query.all()
	# content['category_list'] = set([each.category for each in Actor.query.all()])

	return render_template("category_actor.html", content=content, name=name)











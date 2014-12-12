# -*- coding:utf-8 -*-
from apps.core.model.models import Video, VideoReview

__author__ = 'bebop'

from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response,current_app
from apps import app,db
from apps.core.model import models as models
from sqlalchemy import desc

def video_main():
	#평가인원순
	view_row = {}
	view_row = Video.query.order_by(desc(models.Video.score)).limit(9)
	#평점평균 순서
	rate_row={}
	rate_row = Video.query.order_by(desc(models.Video.score/models.Video.count)).limit(9)
	content={}
	#메인화면에서 카테고리들을 정렬해서 보여주는 부분
	content['category_list'] = set([each.category for each in Video.query.all()])

	return render_template("video_main.html",content=content, view_row=view_row, rate_row=rate_row)

def video_detail(id):
	videoDetail = Video.query.get(id)

	#이미지 가져오기
	videoImage = url_for("show2", key =id)

	#리뷰
	review=videoDetail.videoReview.all()
	if request.method=='POST':
		if not 'session_user_id' in session:
			return redirect(url_for("login"))

		currentReview=VideoReview(
		videoID=id,
		userID=session['session_user_id'],
		content=request.form['content']
		)
		db.session.add(currentReview)
		db.session.commit()
		return redirect(url_for("video_detail", name = id))

	# 출연배우 가져오기
	appearActor={}
	appearActor= videoDetail.video_actor.all()

	average = float(videoDetail.score)/videoDetail.count
	average = float("{0:.2f}".format(average))

	#내 평점 가져오기

	if not 'session_user_id' in session:
		return render_template("video_detail.html", average=average, videoDetail=videoDetail, appearActor=appearActor, review=review, videoImage=videoImage)

	if 'session_user_id' in session:
		ratingExist = videoDetail.rating.filter(models.Rating.userID == session['session_user_id']).first()

	return render_template("video_detail.html", average = average, videoDetail=videoDetail, appearActor=appearActor, ratingExist = ratingExist, review=review, videoImage=videoImage)

#영상 카테고리

def categorize(name):
	content = {}
	content['video_f_list'] = Video.query.filter_by(category=name)

	return render_template("category.html", content=content, name=name)


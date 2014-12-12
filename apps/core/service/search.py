# -*- coding:utf-8 -*-
from flask import render_template, request, redirect
from apps.core.model import models as models

__author__ = 'bebop'
# 디비에 저장된 비디오 검색하기
def search_video():
    if request.method == 'POST':
        video_name = request.form['search_video']
        video_list = models.Video.query.all()
        video_selected = []

        if video_name != "":

            for i in video_list:
                if (i.name.lower()).find(video_name.lower()) != -1:
                    video_selected.append(i.name)

            try:
                video_selected[0]
            except Exception, e:
                video_selected.append(u'해당하는 검색결과가 없습니다.')

            return render_template('search_video.html', video_selected=video_selected, video_name=video_name)

    video_selected.append('Please input video name you find')
    return render_template('search_video.html', video_selected=video_selected, video_name=video_name)



#디비에 저장된 배우 검색하기
def search_actor():
	if request.method == 'POST':

		actor_name = request.form['search_actor']

		actor_list = models.Actor.query.all()
		actor_selected = []

		if actor_name!="":
			for i in actor_list:
				if (i.name).find(actor_name) != -1:
					actor_selected.append(i.name)

			try:
				actor_selected[0]
			except Exception, e:
				actor_selected.append(u'해당하는 검색결과가 없습니다.')

			return render_template('search_actor.html',actor_selected=actor_selected, actor_name=actor_name)

		actor_selected.append('Please input actoress name you find')
		return render_template('search_actor.html',actor_selected=actor_selected, actor_name=actor_name)

# 구글에 + 'torrent' 검색

def crawl():
    if request.method == 'GET':
        basicurl = "https://www.google.co.kr/search?q="
        url = basicurl + request.args['search'] + ' ' + 'torrent'
        return redirect(url)
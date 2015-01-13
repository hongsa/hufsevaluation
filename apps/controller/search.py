# -*- coding: utf-8 -*-
from flask import redirect, render_template, request
from apps.models import Actor, Video

#디비검색
def db_search(searching_word):
    video_list = Video.query.all()
    actor_list = Actor.query.all()
    selected_video = []
    selected_actor = []
    if searching_word != "":
        for i in video_list:
            if (i.name.lower()).find(searching_word.lower()) != -1:
                selected_video.append(i.name)
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

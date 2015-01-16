# -*- coding: utf-8 -*-
from flask import redirect, render_template, request
from apps.models import Actor, Video

#디비검색
def db_search(searching_word):
    video_list = Video.query.all()
    actor_list = Actor.query.all()
    selected_video = []
    selected_actor = []
    #스트링을 쪼개서 리스트에 넣어보기(스페이스있을경우 처리위해)->유저인풋은 리스트가 된다.
    userInput = searching_word.split()

    #검색할 단어가 리스트 내에 존재하는지 검사
    if len(userInput) == 0:
        selected_actor.append(u"검색어를 입력해주세요!")
        return render_template("search_result.html", selected_video=selected_video, selected_actor=selected_actor,
            searching_word=searching_word)

    #스페이스로 쪼갰을때 단어가 두개 든 리스트가 생성된 경우
    elif len(userInput) == 2:
        index0 = userInput[0]
        index1 = userInput[1]
        for i in video_list:
            if (i.name.lower()).find(index0.lower()) != -1:
                if (i.name).find(index1) != -1:
                    selected_video.append(i.name)
        try:
            selected_video[0]
        except Exception, e:

            for j in actor_list:
                if (j.name).find(index0) != -1:
                    if (j.name).find(index1) != -1:
                        selected_actor.append(j.name)
            try:
                selected_actor[0]
            except Exception, e:
                selected_actor.append(u"검색결과가 없습니다.ㅠㅜ")

            return render_template("search_result.html", selected_video=selected_video, selected_actor=selected_actor,
                searching_word=searching_word)
    #스페이스로 쪼개지지 않는 하나의 스트링으로만 검색어가 입력된 경우
    else:
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

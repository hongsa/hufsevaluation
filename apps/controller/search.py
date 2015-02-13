# -*- coding: utf-8 -*-
from flask import redirect, render_template, request
from apps.models import Actor, Video

#디비검색
def db_search(searching_word):

    if len(searching_word) == 0:
        empty = 0
        return render_template("search_result.html", empty=empty,searching_word=searching_word)

    i = searching_word.upper()
    result={}
    result['actor'] = Actor.query.filter(Actor.name.like("%"+i+"%")).with_entities(Actor.name).all()
    result['video'] = Video.query.filter(Video.name.like("%"+i+"%")).with_entities(Video.name).all()

    if result['actor'] == [] and result['video']==[]:
        empty = 0
        return render_template("search_result.html", empty=empty, searching_word=searching_word)

    return render_template("search_result.html",searching_word=searching_word,result=result)


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

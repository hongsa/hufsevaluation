# -*- coding: utf-8 -*-
import math

from flask import redirect, url_for, render_template,flash, session, current_app
from sqlalchemy import desc

from apps.models import Actor,User


def actor_main():
    # 로그인 안한 상태로 오면 index로 빠꾸
    # if not 'session_user_email' in session:
    #     flash(u"로그인 되어있지 않습니다.", "error")
    #     return redirect(url_for('index'))

    totalRank = Actor.query.order_by(desc(Actor.average)).limit(15)
    categoryOne = Actor.query.filter_by(category="1").order_by(desc(Actor.average)).limit(5)
    categoryTwo = Actor.query.filter_by(category="2").order_by(desc(Actor.average)).limit(5)
    categoryThree = Actor.query.filter_by(category="3").order_by(desc(Actor.average)).limit(5)

    return render_template("actor_main.html", totalRank=totalRank, categoryOne=categoryOne, categoryTwo=categoryTwo,
                           categoryThree=categoryThree)


def show2(key):
    actor = Actor.query.get(key)
    mimetype = "image/png"
    return current_app.response_class(actor.image, mimetype=mimetype)

import logging
def actor_category(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    # if not 'session_user_email' in session:
    #     flash(u"로그인 되어있지 않습니다.", "error")
    #     return redirect(url_for('index'))

    actor = Actor.query.filter_by(category=name)
    actorCategory = actor.order_by(desc(Actor.average)).offset(
        (page - 1) * 12).limit(12)
    category = actor.first().category

    total = actor.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingsActor()

    list = []
    for i in actorCategory:
        list.append(i.name)

    ratingList=[]
    for r in rating:
        if r['name'] in list:
            ratingList.append(dict(name = r['name'], rating=r['rating']))


    a = float(math.ceil(float(page)/10))
    if a ==1:
        down=1
    else:
        down = int((a-1) * 10)

    if total_page > a*10:
        total_page = a * 10
        up = int(total_page+1)

    else:
        up = int(total_page)

    return render_template("actor_category.html", actorCategory=actorCategory, category=category,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page)

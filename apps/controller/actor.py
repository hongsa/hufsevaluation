# -*- coding: utf-8 -*-
import math

from flask import redirect, url_for, render_template,flash, session, current_app
from sqlalchemy import desc

from apps.models import Actor,User,ActorReview
# from werkzeug.contrib.cache import GAEMemcachedCache
import logging

def actor_main():
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    totalRank = Actor.query.order_by(desc(Actor.average)).with_entities(Actor.name).limit(15)

    content = {}
    content['one'] = Actor.query.filter(Actor.category=="1",Actor.count>10).order_by(desc(Actor.average))\
        .with_entities(Actor.name,Actor.average).limit(5)
    content['two'] = Actor.query.filter(Actor.category=="2",Actor.count>10).order_by(desc(Actor.average))\
        .with_entities(Actor.name,Actor.average).limit(5)
    content['three'] = Actor.query.filter(Actor.category=="3",Actor.count>10).order_by(desc(Actor.average))\
        .with_entities(Actor.name,Actor.average).limit(5)
    content['four'] = Actor.query.filter(Actor.category=="4",Actor.count>10).order_by(desc(Actor.average))\
        .with_entities(Actor.name,Actor.average).limit(5)

    review = ActorReview.query.order_by(desc(ActorReview.id)).limit(40)



    return render_template("actor_main.html", totalRank=totalRank, content=content,review=review)



# def show2(key):
#     cache = GAEMemcachedCache()
#     rv = cache.get(key)
#
#     if rv is None:
#         rv = Actor.query.get(key).image
#         cache.set(key, rv, timeout=60 * 60 * 24)
        # actor = Actor.query.get(key)

    # else:
    #     actor = Actor.query.get(rv)

    # mimetype = "image/png"
    # return current_app.response_class(rv, mimetype=mimetype)

def actor_category(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    actor = Actor.query.filter_by(category=name)
    actorCategory = actor.order_by(desc(Actor.average)).offset(
        (page - 1) * 12).with_entities(Actor.name,Actor.average,Actor.count).limit(12)
    # category = actor.first().category

    if name=='1':
        category="진짜 작은애당"
    elif name=='2':
        category="품에 쏘오오옥"
    elif name=='3':
        category="걸그룹 키당"
    else:
        category="힐 신지 말아조"


    total = actor.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingActor_user
    # logging.error(rating)


    list = []
    for i in actorCategory:
        list.append(i.name)

    ratingList=[]
    for r in rating:
        if r.actorName in list:
            ratingList.append(dict(name = r.actorName, rating=r.rating))


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
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page,name=name)

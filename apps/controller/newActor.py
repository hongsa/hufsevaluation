# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, flash, session
from apps.models import Actor,User
from sqlalchemy import desc
import math


def new_actor(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    releaseList = set([int(each.release) for each in Actor.query.with_entities(Actor.release)])
    actor = Actor.query.filter(Actor.release * 100 >= name * 100,
                                      Actor.release * 100 <= (name + 1) * 100)
    actorRelease = actor.order_by(desc(Actor.release)).offset((page - 1) * 12)\
        .with_entities(Actor.name,Actor.average,Actor.count).limit(12)
    total = actor.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    if name == 0:
        release = 0
        actorRelease = Actor.query.filter_by(release=0).offset((page - 1) * 12)\
            .with_entities(Actor.name,Actor.average,Actor.count).limit(12)
        total = Actor.query.filter_by(release=0).count()
        calclulate = float(float(total) / 12)
        total_page = math.ceil(calclulate)

    else:
        release = int(actor.first().release)

    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingActor_user

    list = []
    for v in actorRelease:
        list.append(v.name)

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


    return render_template("new_actor_main.html", releaseList=releaseList, actorRelease=actorRelease, release=release,
            total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page)

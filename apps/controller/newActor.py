# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, flash, session
from apps.models import Actor
from sqlalchemy import desc
import math


def new_actor(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    releaseList = set([int(each.release) for each in Actor.query.all()])
    # logging.error(releaseList)
    actorRelease = Actor.query.filter(Actor.release * 100 > name * 100,
                                      Actor.release * 100 < (name + 1) * 100).order_by(desc(Actor.release)).offset(
    (page - 1) * 12).limit(12)
    # logging.error(actorRelease)
    total = Actor.query.filter(Actor.release * 100 > name * 100, Actor.release * 100 < (name + 1) * 100).count()
    # logging.error(total)
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    if name == 0:
        release = 0
        actorRelease = Actor.query.filter_by(release=0).offset((page - 1) * 12).limit(12)
    else:
        release = int(Actor.query.filter(Actor.release * 100 > name * 100, Actor.release * 100 < (name + 1) * 100).first().release)



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
            total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down)

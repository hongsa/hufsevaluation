# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, flash, session,current_app
from apps.models import Video,User
from sqlalchemy import desc
import math
from werkzeug.contrib.cache import GAEMemcachedCache

def video_main():
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    totalRank = Video.query.order_by(desc(Video.average)).limit(15)
    categoryOne = Video.query.filter_by(category="1").order_by(desc(Video.average)).limit(5)
    categoryTwo = Video.query.filter_by(category="2").order_by(desc(Video.average)).limit(5)
    categoryThree = Video.query.filter_by(category="3").order_by(desc(Video.average)).limit(5)
    categoryFour = Video.query.filter_by(category="4").order_by(desc(Video.average)).limit(5)
    categoryFive = Video.query.filter_by(category="5").order_by(desc(Video.average)).limit(5)
    categorySix = Video.query.filter_by(category="6").order_by(desc(Video.average)).limit(5)

    return render_template("video_main.html", totalRank=totalRank, categoryOne=categoryOne, categoryTwo=categoryTwo,
                           categoryThree=categoryThree, categoryFour=categoryFour, categoryFive=categoryFive,categorySix=categorySix)

import logging
def video_category(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    video = Video.query.filter_by(category=name)
    videoCategory = video.order_by(desc(Video.average)).offset(
        (page - 1) * 12).limit(12)
    total = video.count()

    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    category = video.first().category

    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingsVideo()

    list = []
    for v in videoCategory:
        list.append(v.name)

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

    return render_template("video_category.html", videoCategory=videoCategory, category=category,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page)


# def show1(key):
#     cache = GAEMemcachedCache()
#     rv = cache.get(key)
#
#     if rv is None:
#         rv = Video.query.get(key).image
#         cache.set(key, rv, timeout=60 * 60 * 24)
        # actor = Actor.query.get(key)

    # else:
    #     actor = Actor.query.get(rv)

    # mimetype = "image/png"
    # return current_app.response_class(rv, mimetype=mimetype)
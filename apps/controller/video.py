# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, flash, session,current_app
from apps.models import Video,User,VideoReview
from sqlalchemy import desc
import math
from werkzeug.contrib.cache import GAEMemcachedCache
import random

def video_main():
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    # totalRank = Video.query.filter(Video.count>10).order_by(desc(Video.average)).with_entities(Video.name).limit(15)

    content={}
    content['one'] = Video.query.filter(Video.category=="1",Video.count>10).order_by(desc(Video.average))\
        .with_entities(Video.name,Video.average).limit(5)
    content['two'] = Video.query.filter(Video.category=="2",Video.count>10).order_by(desc(Video.average))\
        .with_entities(Video.name,Video.average).limit(5).limit(5)
    content['three'] = Video.query.filter(Video.category=="3",Video.count>10).order_by(desc(Video.average))\
        .with_entities(Video.name,Video.average).limit(5).limit(5)
    content['four'] = Video.query.filter(Video.category=="4",Video.count>10).order_by(desc(Video.average))\
        .with_entities(Video.name,Video.average).limit(5).limit(5)
    content['five'] = Video.query.filter(Video.category=="5",Video.count>10).order_by(desc(Video.average))\
        .with_entities(Video.name,Video.average).limit(5).limit(5)
    content['six'] = Video.query.filter(Video.category=="6",Video.count>10).order_by(desc(Video.average))\
        .with_entities(Video.name,Video.average).limit(5).limit(5)

    review = VideoReview.query.order_by(desc(VideoReview.id)).limit(40)
    number = random.randint(1,3)

    return render_template("video_main.html", content=content,review=review,number=number)

import logging
def video_category(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    video = Video.query.filter_by(category=name)
    # videoCategory = video.order_by(desc(Video.average)).offset(
    #     (page - 1) * 12).with_entities(Video.name,Video.average,Video.count).limit(12)
    videoCategory = video.order_by(desc(Video.average)).offset((page - 1) * 12).limit(12)
    total = video.count()

    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    if name=='1':
        category="러브 액츄얼리"
    elif name=='2':
        category="금지된 사랑"
    elif name=='3':
        category="코스튬"
    elif name=='4':
        category="협동조합"
    elif name=='5':
        category="상황극"
    else:
        category ="온천물"


    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingVideo_user

    list = []
    for v in videoCategory:
        list.append(v.name)

    ratingList=[]
    for r in rating:
        if r.videoName in list:
            ratingList.append(dict(name = r.videoName, rating=r.rating))


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

    number = random.randint(1,3)

    return render_template("video_category.html", videoCategory=videoCategory, category=category,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page,name=name,number=number)


def video_category2(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    video = Video.query.filter_by(category=name)
    # videoCategory = video.order_by(desc(Video.count)).offset(
    #     (page - 1) * 12).with_entities(Video.name,Video.average,Video.count).limit(12)

    videoCategory = video.order_by(desc(Video.count)).offset((page - 1) * 12).limit(12)

    total = video.count()

    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    if name=='1':
        category="러브 액츄얼리"
    elif name=='2':
        category="금지된 사랑"
    elif name=='3':
        category="코스튬"
    elif name=='4':
        category="협동조합"
    elif name=='5':
        category="상황극"
    else:
        category ="온천물"


    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingVideo_user

    list = []
    for v in videoCategory:
        list.append(v.name)

    ratingList=[]
    for r in rating:
        if r.videoName in list:
            ratingList.append(dict(name = r.videoName, rating=r.rating))


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

    number = random.randint(1,3)

    return render_template("video_category2.html", videoCategory=videoCategory, category=category,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page,name=name,number=number)



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
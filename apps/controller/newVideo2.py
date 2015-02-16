# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template,flash, session
from apps.models import Video,User
from sqlalchemy import desc
import math


def new_video2(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    releaseList = set([int(each.release) for each in Video.query.with_entities(Video.release)])
    video = Video.query.filter(Video.release * 100 > name * 100,
                                      Video.release * 100 < (name + 1) * 100)
    videoRelease = video.order_by(desc(Video.release)).offset((page - 1) * 12)\
        .with_entities(Video.name,Video.average,Video.count).limit(12)
    total = video.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

    if name == 0:
        release = 0
        videoRelease = Video.query.filter_by(release=0).offset((page - 1) * 12)\
            .with_entities(Video.name,Video.average,Video.count).limit(12)
    else:
        release = int(video.first().release)

    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingsActor()

    list = []
    for v in videoRelease:
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


    return render_template("new_video_main2.html", releaseList=releaseList, videoRelease=videoRelease, release=release,
            total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page)

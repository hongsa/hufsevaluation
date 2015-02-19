# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template,flash, session
from apps.models import Video,User
from sqlalchemy import desc
import math

def new_video(name, page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    companyList = set([each.company for each in Video.query.with_entities(Video.company).all()])
    video = Video.query.filter_by(company=name)
    videoCompany = video.order_by(desc(Video.release)).offset(
        (page - 1) * 12).with_entities(Video.name,Video.average,Video.count).limit(12)
    total = video.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)
    company = video.first().company

    email = session['session_user_email']
    user = User.query.get(email)
    rating = user.ratingVideo_user

    list = []
    for v in videoCompany:
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

    return render_template("new_video_main.html", companyList=companyList, videoCompany=videoCompany, company=company,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,ratingList=ratingList,page=page)
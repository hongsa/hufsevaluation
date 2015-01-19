# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template,flash, session
from apps.models import User,RatingActor, RatingVideo
import math

def actor_collection_bookmark(page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    user = User.query.get(email)
    myBookmark = user.favorite_user.offset((page - 1) * 12).limit(12)
    total = user.favorite_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

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

    return render_template("actor_collection_bookmark.html", myBookmark=myBookmark,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down, page=page)


def actor_collection_rating(page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    user = User.query.get(email)
    myRating = user.ratingActor_user.order_by(RatingActor.rating.desc()).offset((page - 1) * 12).limit(12)
    total = user.ratingActor_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

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

    return render_template("actor_collection_rating.html", myRating=myRating,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down, page=page)


def video_collection_bookmark(page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    user = User.query.get(email)
    myBookmark = user.bookmark_user.offset((page - 1) * 12).limit(12)
    total = user.bookmark_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

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

    return render_template("video_collection_bookmark.html", myBookmark=myBookmark,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down, page=page)


def video_collection_rating(page):
    # 로그인 안한 상태로 오면 index로 빠꾸
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    user = User.query.get(email)
    myRating = user.ratingVideo_user.order_by(RatingVideo.rating.desc()).offset((page - 1) * 12).limit(12)
    total = user.ratingVideo_user.count()
    calclulate = float(float(total) / 12)
    total_page = math.ceil(calclulate)

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

    return render_template("video_collection_rating.html", myRating=myRating,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,page=page)


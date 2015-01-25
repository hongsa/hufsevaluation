# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, request, flash, session
from apps import db
from apps.models import User, Actor, Video, Filmo

def admin_main():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        return render_template("admin.html")

    return redirect(url_for("index"))


def admin_actor():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:

        if request.method == 'POST':
            files = request.files['actor_image']
            filestream = files.read()

            actor_write = Actor(
                name=request.form['name'],
                image=filestream,
                category=request.form['category'],
                age=request.form['age'],
                release=request.form['release']
            )
            db.session.add(actor_write)
            db.session.commit()
            flash(u"배우 DB에 저장되었습니다.")
            return redirect(url_for("admin_main"))

        return render_template("admin.html")

    return redirect(url_for("index"))


def admin_actor_check():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            name = request.form['name']
            actor = Actor.query.get(name)
            if actor:
                flash(u"이미 있는 배우입니다.")
                return redirect(url_for("admin_main"))
            else:
                flash(u"없는 배우입니다.")
                return redirect(url_for("admin_main"))

    return redirect(url_for("index"))


def admin_video():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            files = request.files['video_image']
            filestream = files.read()

            video_write = Video(
                name=request.form['name'],
                image=filestream,
                category=request.form['category'],
                company=request.form['company'],
                release=request.form['release'],
                exposure=request.form['exposure']
            )
            db.session.add(video_write)
            db.session.commit()

            flash(u"영상 DB에 저장되었습니다.")
            return redirect(url_for("admin_main"))

        return render_template("admin.html")

    return redirect(url_for("index"))

def admin_video_check():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            name = request.form['name']
            video = Video.query.get(name)
            if video:
                flash(u"이미 있는 품번입니다.")
                return redirect(url_for("admin_main"))
            else:
                flash(u"없는 품번입니다.")
                return redirect(url_for("admin_main"))

def admin_connect():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            connect = Filmo(
                ActorName=request.form['actor_name'],
                videoName=request.form['video_name']
            )
            db.session.add(connect)
            db.session.commit()
            flash(u"잘 연결되었습니다.")

            return redirect(url_for("admin_main"))

        return render_template("admin.html")

    return redirect(url_for("index"))

def admin_edit():
    email = session['session_user_email']
    user = User.query.get(email)

    if user.level == 1:
        if request.method == 'POST':
            name = request.form['name']
            actor = Actor.query.get(name)
            actor.category = request.form['height']
            db.session.commit()
            flash(u"수정 완료")

            return redirect(url_for("admin_main"))
        return render_template("admin.html")
    return render_template(url_for("index"))


def admin_a_img():

    email = session['session_user_email']
    user = User.query.get(email)
    files = request.files['img']
    filestream = files.read()

    if user.level == 1:
        if request.method == 'POST':
            name = request.form['name']
            actor = Actor.query.get(name)
            actor.image = filestream
            db.session.commit()
            flash(u"이미지 수정 완료")

            return redirect(url_for("admin_main"))
        return render_template("admin.html")
    return render_template(url_for("index"))

def admin_v_img():

    email = session['session_user_email']
    user = User.query.get(email)
    files = request.files['img']
    filestream = files.read()

    if user.level == 1:
        if request.method == 'POST':
            name = request.form['name']
            video = Video.query.get(name)
            video.image = filestream
            db.session.commit()
            flash(u"이미지 수정 완료")

            return redirect(url_for("admin_main"))
        return render_template("admin.html")
    return render_template(url_for("index"))
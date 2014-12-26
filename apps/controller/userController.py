# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response, \
    current_app
from apps import app, db, models
from werkzeug.security import generate_password_hash, check_password_hash
from apps.models import User, Actor, Video, ActorReview, VideoReview, Filmo, RatingActor, RatingVideo, Favorite, Bookmark
from sqlalchemy import desc
from apps import forms
import math
import json


def index():
    if not 'session_user_email' in session:
        form=forms.JoinForm()
        form2=forms.LoginForm()
        session['if_confirm'] = "true"
        return render_template("main_page.html", form=form,form2=form2)
    return redirect(url_for('actor_main'))


# 회원가입
def signup():

    form = forms.JoinForm()
    form2 = forms.LoginForm()

    try:
        if session['session_user_email']:
            flash(u"이미 회원가입 하셨습니다!", "error")
            return render_template("main_page.html", form=form, form2=form2)
    except Exception, e:
        pass

    if request.method == 'POST':
        if User.query.get(form.email.data):
            session.clear()
            flash(u"이미 등록된 메일 주소 입니다!", "error")
            return render_template("main_page.html", form=form, form2=form2)
        if User.query.get(form.nickname.data):
            session.clear()
            flash(u"이미 사용중인 닉네임입니다!", "error")
            return render_template("main_page.html", form=form, form2=form2)
        if not form.validate_on_submit():
            session.clear()
            flash(u"올바른 형식으로 입력해주세요!", "error")
            return render_template("main_page.html", form=form, form2=form2)

        user = User(email=form.email.data, password=generate_password_hash(form.password.data),
                    nickname=form.nickname.data, sex=form.sex.data)

        db.session.add(user)
        db.session.commit()

        session.clear()

        # flash(u"회원가입 되셨습니다!")
        session['session_user_email'] = form.email.data
        session['session_user_nickname'] = form.nickname.data

        return redirect(url_for('actor_main'))

    session.clear()
    flash(u"잘못 입력하셨습니다!","error")
    return render_template("main_page.html", form=form, form2=form2)



#로그인
def login():

    form = forms.JoinForm()
    form2 = forms.LoginForm()

    try:
        if session['session_user_email']:
            flash(u'이미 로그인 하셨습니다!', "error")
            return redirect(url_for('actor_main'))

    except Exception, e:
        pass


    if request.method == "POST":
        if form2.validate_on_submit():
            email = form.email.data
            pwd = form.password.data
            user = User.query.get(email)
            if user is None:
                session.clear()
                flash(u"존재하지 않는 이메일 입니다.", "error")
                return render_template("main_page.html", form=form, form2=form2)
            elif not check_password_hash(user.password, pwd):
                session.clear()
                flash(u"비밀번호가 일치하지 않습니다.", "error")
                return render_template("main_page.html", form=form, form2=form2)
            else:
                session.permanent = True
                session['session_user_email'] = user.email
                session['session_user_nickname'] = user.nickname
                return redirect(url_for('actor_main'))


    session.clear()

    flash(u"잘못 입력하셨습니다!","error")

    return render_template("main_page.html", form=form, form2=form2)

#로그아웃 부분.
def logout():

    if "session_user_email" in session:
        session.clear()
        # flash(u"로그아웃 되었습니다.")
    else:
        flash(u"로그인 되어있지 않습니다.", "error")
    return redirect(url_for('index'))

def modify_password():
    if request.method == 'POST':
        email = session['session_user_email']
        user= User.query.get(email)
        user.password = generate_password_hash(request.form['password'])
        db.session.commit()
        flash(u"변경 완료되었습니다.", "password")
        return redirect(url_for('modify_password'))

    return render_template("modify.html")

def modify_nickname():
    if request.method == 'POST':
        email = session['session_user_email']
        user= User.query.get(email)

        nickname=request.form['nickname']
        nickname_list=[]
        for i in User.query.all():
		    nickname_list.append(i.nickname)
        if nickname in nickname_list:
            flash(u"이미 사용 중인 닉네임 입니다.", "nickname")
            return redirect(url_for('modify_nickname'))

        user.nickname=nickname
        db.session.commit()
        session['session_user_nickname'] = user.nickname
        flash(u"변경 완료되었습니다.", "nickname")
        return redirect(url_for('modify_nickname'))

    return render_template("modify.html")
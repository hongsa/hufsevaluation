# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, request, flash, session
from apps import db
from werkzeug.security import generate_password_hash, check_password_hash
from apps.models import User
from apps import forms
import random
import pytz
import datetime

def get_current_time():
    return datetime.datetime.now(pytz.timezone('Asia/Seoul'))


def index():
    if not 'session_user_code' in session:
        return render_template("index.html")
    return redirect(url_for('search'))


# 회원가입
def signup():
    number = random.randint(1,4)
    form = forms.JoinForm()

    try:
        if session['session_user_code']:
            flash(u"이미 회원가입 하셨습니다!", "error")
            return render_template("signup.html", form=form)
    except Exception, e:
        pass


    if request.method == 'POST':
        if User.query.filter_by(code=form.code.data).first():
            flash(u"이미 등록된 학번 입니다!", "error")
            return render_template("signup.html", form=form)
        if not len(form.code.data) ==9:
            flash(u"제대로된 학번이 아닙니다!", "error")
            return render_template("signup.html", form=form)

        if User.query.filter_by(nickname=form.nickname.data).first():
            flash(u"이미 사용중인 닉네임입니다!", "error")
            return render_template("signup.html", form=form)
        if not form.validate_on_submit():
            flash(u"올바른 형식으로 입력해주세요!", "error")
            return render_template("signup.html", form=form)

        user = User(code = form.code.data, password=generate_password_hash(form.password.data),
                    nickname=form.nickname.data, sex=form.sex.data,college= form.college.data,joinDATE=get_current_time())

        db.session.add(user)
        db.session.commit()

        session['session_user_code'] = form.code.data
        session['session_user_nickname'] = form.nickname.data

        return redirect(url_for('search'))

    return render_template("signup.html", form=form,number=number)



#로그인
def login():

    form = forms.LoginForm()

    try:
        if session['session_user_code']:
            flash(u'이미 로그인 하셨습니다!', "error")
            return redirect(url_for('search'))

    except Exception, e:
        pass


    if request.method == "POST":
        if form.validate_on_submit():
            code = form.code.data
            pwd = form.password.data
            user = User.query.filter_by(code=code).first()
            if user is None:
                flash(u"존재하지 않는 학번입니다.", "error")
                return render_template("login.html", form=form)
            elif not check_password_hash(user.password, pwd):
                flash(u"비밀번호가 틀렸습니다!", "error")
                return render_template("login.html", form=form)
            else:
                session.permanent = True
                session['session_user_code'] = user.code
                session['session_user_nickname'] = user.nickname
                return redirect(url_for('search'))


    return render_template("login.html", form=form)

#로그아웃 부분.
def logout():

    if "session_user_code" in session:
        session.clear()
    else:
        flash(u"로그인 되어있지 않습니다.", "error")
    return redirect(url_for('index'))

def modify_password():

    user = User.query.filter_by(code=session['session_user_code']).first()

    if request.method == 'POST':
        user.password = generate_password_hash(request.form['password'])
        db.session.commit()
        flash(u"변경 완료되었습니다.", "password")
        return redirect(url_for('modify_password'))

    return render_template("modify.html")

def modify_nickname():

    user = User.query.filter_by(code=session['session_user_code']).first()

    if request.method == 'POST':
        nickname=request.form['nickname']
        if len(nickname) >=8:
            flash(u"7자 이내로 입력해주세요.", "nickname")
            return redirect(url_for('modify_nickname'))


        if User.query.filter_by(nickname=nickname).first():
            flash(u"이미 사용 중인 닉네임 입니다.", "nickname")
            return redirect(url_for('modify_nickname'))

        user.nickname=nickname
        db.session.commit()
        session['session_user_nickname'] = user.nickname
        flash(u"변경 완료되었습니다.", "nickname")
        return redirect(url_for('modify_nickname'))

    return render_template("modify.html")


def contact():
    return render_template("contact.html")
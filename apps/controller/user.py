# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template, request, flash, session
from apps import db
from werkzeug.security import generate_password_hash, check_password_hash
from apps.models import User
from apps import forms
import random
import logging

def index():
    number = random.randint(1,5)
    if not 'session_user_email' in session:
        form=forms.LoginForm()
        return render_template("mainPageNew.html", form=form, number=number)
    return redirect(url_for('actor_main'))


# 회원가입
def signup():
    number = random.randint(1,5)
    form = forms.JoinForm()

    # nickname_list=[]
    # for i in User.query.with_entities(User.nickname).all():
    #     nickname_list.append(i.nickname)
    try:
        if session['session_user_email']:
            flash(u"이미 회원가입 하셨습니다!", "error")
            return render_template("signup.html", form=form)
    except Exception, e:
        pass


    if request.method == 'POST':
        if User.query.get(form.email.data):
            flash(u"이미 등록된 메일 주소 입니다!", "error")
            return render_template("signup.html", form=form)
        if User.query.filter_by(nickname=form.nickname.data).first():
            flash(u"이미 사용중인 닉네임입니다!", "error")
            return render_template("signup.html", form=form)
        if not form.validate_on_submit():
            flash(u"올바른 형식으로 입력해주세요!", "error")
            return render_template("signup.html", form=form)

        user = User(email=form.email.data, password=generate_password_hash(form.password.data),
                    nickname=form.nickname.data, sex=form.sex.data)

        db.session.add(user)
        db.session.commit()


        # flash(u"회원가입 되셨습니다!")
        session['session_user_email'] = form.email.data
        session['session_user_nickname'] = form.nickname.data

        return redirect(url_for('actor_main'))

    return render_template("signup.html", form=form,number=number)



#로그인
def login():
    
    form = forms.LoginForm()

    try:
        if session['session_user_email']:
            flash(u'이미 로그인 하셨습니다!', "error")
            return redirect(url_for('actor_main'))

    except Exception, e:
        pass


    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            pwd = form.password.data
            user = User.query.get(email)
            if user is None:
                flash(u"존재하지 않는 이메일 입니다.", "error")
                return render_template("mainPageNew.html", form=form)
            elif not check_password_hash(user.password, pwd):
                flash(u"비밀번호가 틀렸습니다!", "error")
                return render_template("mainPageNew.html", form=form)
            else:
                session.permanent = True
                session['session_user_email'] = user.email
                session['session_user_nickname'] = user.nickname
                return redirect(url_for('actor_main'))


    return render_template("mainPageNew.html", form=form)

#로그아웃 부분.
def logout():

    if "session_user_email" in session:
        session.clear()
        # flash(u"로그아웃 되었습니다.")
    else:
        flash(u"로그인 되어있지 않습니다.", "error")
    return redirect(url_for('index'))

def modify_password():
    email = session['session_user_email']
    user= User.query.get(email)
    level = user.level
    if request.method == 'POST':
        user.password = generate_password_hash(request.form['password'])
        db.session.commit()
        flash(u"변경 완료되었습니다.", "password")
        return redirect(url_for('modify_password'))

    return render_template("modify.html",level=level)

def modify_nickname():
    email = session['session_user_email']
    user= User.query.get(email)
    level=user.level
    if request.method == 'POST':
        nickname=request.form['nickname']
        if len(nickname) >=8:
            flash(u"7자 이내로 입력해주세요.", "nickname")
            return redirect(url_for('modify_nickname'))

        # nickname_list=[]
        # for i in User.query.with_entities(User.nickname).all():
        #     nickname_list.append(i.nickname)
        # if nickname in nickname_list:


        if User.query.filter_by(nickname=nickname).first():
            flash(u"이미 사용 중인 닉네임 입니다.", "nickname")
            return redirect(url_for('modify_nickname'))

        user.nickname=nickname
        db.session.commit()
        session['session_user_nickname'] = user.nickname
        flash(u"변경 완료되었습니다.", "nickname")
        return redirect(url_for('modify_nickname'))

    return render_template("modify.html", level=level)


def contact():
    return render_template("contact.html")
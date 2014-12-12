# -*- coding:utf-8 -*-
from apps.core.model.models import Rating, Bookmark, Actor

__author__ = 'bebop'
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response, \
    current_app
from werkzeug.security import generate_password_hash, check_password_hash
from apps import app, db
from apps.core.model import models as models
from apps.core.service import forms as forms


# 회원가입 부분입니다.
def signup():


    try:
        
        if session['session_user_email']:

            flash(u'이미 회원가입 하셨습니다!')
            return redirect(url_for('index'))

    except Exception, e:
        pass

    form = forms.JoinForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(u'adf')
            return render_template("signup.html", form=form)
        if models.User.query.get(request.form['email']):
            flash(u'이미 등록된 이메일 주소입니다.', "error")
            return render_template('signup.html', form=form)
        nickname_list = []
        for i in models.User.query.all():
            nickname_list.append(i.nickname)
        if form.nickname.data in nickname_list:
            flash(u"이미 사용 중인 닉네임 입니다.", "error")
            return render_template("signup.html", form=form)
        user = models.User(email=form.email.data, password=generate_password_hash(form.password.data),
                           nickname=form.nickname.data)
        db.session.add(user)
        db.session.commit()
        flash(u"회원가입 되었습니다!", "success")

        session['session_user_email'] = form.email.data
        session['session_user_nickname'] = form.nickname.data
        
        return redirect(url_for('index'))
    # return render_template("main.html")
    return render_template('signup.html', form=form)


#로그인 부분입니다.
def login():


    try:
        
        if session['session_user_email']:

            flash(u'이미 로그인 하셨습니다!')
            return redirect(url_for('index'))

    except Exception, e:
        pass

    form = forms.LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            pwd = form.password.data
            user = models.User.query.get(email)
            if user is None:
                flash(u"존재하지 않는 이메일 입니다.", "error")
            elif not check_password_hash(user.password, pwd):
                flash(u"비밀번호가 일치하지 않습니다.", "error")
            else:
                session.permanent = True
                session['session_user_id'] = user.id
                session['session_user_nickname'] = user.nickname

                flash(u"로그인 되었습니다!", "success")
                return redirect(url_for('index'))
    return render_template("login.html", form=form)


#로그아웃 부분입니다.
def logout():
    if "session_user_id" in session:
        session.clear()
        flash(u"로그아웃 되었습니다.", "success")
    else:
        flash(u"로그인 되어있지 않습니다.", "error")
    return redirect(url_for('index'))


#마이페이지 정보입니다.
def current_user():
    currentID = session['session_user_id']
    return models.User.query.get(currentID)

def my_page():
    if not 'session_user_id' in session:
        return redirect(url_for("login"))

    user = current_user()
    myRating = user.rating.order_by(models.Rating.rating.desc()).all()
    myBookmark = user.user_bookmark.all()

    return render_template("my_page.html", myRating = myRating, myBookmark = myBookmark)

def favoriteActor(id):
    actor = models.Actor.query.get(id)

    if not 'session_user_id' in session:
        return redirect(url_for('login'))

    user = current_user()
    bookmark_exist = user.user_bookmark.filter(actor.name==models.Bookmark.actor_name).first()
    
    if bookmark_exist:
        return redirect(url_for("actress_detail",id=id))

    myFavorite=models.Favorite(
        actorID=actor.id,
        userID=session['session_user_id']
        )
    db.session.add(myFavorite)
    db.session.commit()

    return redirect(url_for("actress_detail",id=id))

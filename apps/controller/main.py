# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template,flash, session, request,g
from apps.models import Rating,Lecture,User
from apps import db,app
from werkzeug.security import generate_password_hash, check_password_hash

def search():

    if request.method == "POST":
        search = str(request.form['search'])

        if len(search) == 0:
            empty = 0
            return render_template("search.html", empty=empty,search=search)

        lecture={}
        lecture['name'] = Lecture.query.filter(Lecture.name.like("%"+search+"%")).outerjoin(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).group_by(Lecture.id).all()
        lecture['professor'] = Lecture.query.filter(Lecture.professor.like("%"+search+"%")).outerjoin(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).group_by(Lecture.id).all()

        if lecture['name'] == [] and lecture['professor']==[]:
            empty = 0
            return render_template("search.html", empty=empty, search=search)
        else:
            return render_template("search.html", lecture=lecture, search=search)

    empty=1
    return render_template("search.html", empty=empty)

def search2():

    if request.method == "POST":
        year = int(request.form['year'])
        semester = int(request.form['semester'])
        category1 = request.form['category1']
        category2 = request.form['category2']
        category=""

        if category1 == "0":
            category = category2
        else :
            category = category1

        if semester == 3:
            lecture = Lecture.query.filter(Lecture.category==category, Lecture.year == year).outerjoin(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).group_by(Lecture.id).all()
        else:
            lecture = Lecture.query.filter(Lecture.category==category,Lecture.semester == semester,Lecture.year == year).outerjoin(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).group_by(Lecture.id).all()

        return render_template("search2.html",lecture=lecture,category=category)
    return redirect(url_for('search'))


def detail(id):


    list = [str(i) for i in str(g.user.code)]

    if int(list[2]+list[3]) == 16:
        pass
    elif g.user.count < 5:
        flash(u"평가를 5개 이상 해주세요.", "error")
        return redirect(url_for('search'))

    detail = Lecture.query.get(id)
    rating = detail.rating_lecture.all()

    return render_template("detail.html",detail=detail, rating = rating)

def admin():

    if request.method == "POST":
        name = request.form['name']
        professor = request.form['professor']
        year = int(request.form['year'])
        semester = int(request.form['semester'])
        category = request.form['category']
        get_grade = int(request.form['get_grade'])

        exist= Lecture.query.filter_by(name=name,professor=professor,semester=semester,year=year).first()

        if exist:
            flash("중복입니다.")
            return render_template("admin.html")

        lecture = Lecture(name=name,professor=professor,year=year,semester=semester,category=category,get_grade=get_grade)
        db.session.add(lecture)
        db.session.commit()

        flash(name + professor)
        return render_template("admin.html")

    if g.user.level == 1:

        return render_template("admin.html")

    else:
        return redirect(url_for('index'))

def admin_pw():

    if request.method == "POST":

        code = request.form['code']
        pw = request.form['pw']
        reset = User.query.filter(User.code == code).first()
        reset.password =generate_password_hash(pw)
        db.session.commit()
        return redirect(url_for('admin'))


def admin_auth():

    if request.method == "POST":

        auth = request.form['auth']
        level = User.query.filter(User.code == auth).first()
        level.level = 1
        db.session.commit()
        return redirect(url_for('admin'))
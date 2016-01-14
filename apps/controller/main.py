# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template,flash, session, request
from apps.models import Rating,Lecture,User
from apps import db

def search():

    if not 'session_user_code' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    if request.method == "POST":

        search = request.form['search']
        if len(search) == 0:
            empty = 0
            return render_template("search.html", empty=empty,search=search)

        lecture={}

        lecture['name'] = Lecture.query.filter(Lecture.name.like("%"+search+"%")).join(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).all()
        lecture['professor'] = Lecture.query.filter(Lecture.professor.like("%"+search+"%")).join(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).all()

        if lecture['name'] == [] and lecture['professor']==[]:
            empty = 0
            return render_template("search.html", empty=empty, search=search)

        else:
            return render_template("search.html", lecture=lecture, search=search)

    empty=1
    return render_template("search.html", empty=empty)


def search2():

    if not 'session_user_code' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

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
            lecture = Lecture.query.filter(Lecture.category==category, Lecture.year == year).join(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).all()


        else:
            lecture = Lecture.query.filter(Lecture.category==category, Lecture.year == year, Lecture.semester == semester).join(Rating, Lecture.id==Rating.lecture_id).add_columns(Rating.opinion).all()


        return render_template("search2.html",lecture=lecture,category=category)


def detail(id):

    if not 'session_user_code' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    user = User.query.filter_by(code=session['session_user_code']).first()

    list = [str(i) for i in str(user.code)]

    if int(list[2]+list[3]) == 16:
        pass

    elif user.count < 5:
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
    return render_template("admin.html")



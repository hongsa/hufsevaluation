# -*- coding: utf-8 -*-
from flask import redirect, url_for, render_template,flash, session, request,jsonify,g
from sqlalchemy import desc
from apps.models import Rating,User,Lecture
from apps.controller.pagination import pagination
from apps import db


def my_rating(page):

    user = User.query.filter_by(code=session['session_user_code']).first()
    my_rating = user.rating_user.order_by(desc(Rating.joinDATE)).offset((page - 1) * 8).limit(8)
    total = user.rating_user.count()

    paging = pagination(total,page)
    up = paging.up()
    down = paging.down()
    total_page = paging.totalCount()

    return render_template("my_rating.html",my_rating=my_rating, total_page=total_page, up = up, down = down, page=page)

def delete(id):

    rating = Rating.query.get(id)
    lecture = Lecture.query.get(rating.lecture_id)
    user = User.query.filter_by(code=session['session_user_code']).first()
    user.count-=1

    lecture.total -=rating.total
    lecture.difficulty-=rating.difficulty
    lecture.study_time-=rating.study_time
    lecture.attendance-=rating.attendance
    lecture.grade-=rating.grade
    lecture.achievement-=rating.achievement
    lecture.count-=1

    db.session.delete(rating)
    db.session.commit()

    return redirect(url_for("my_rating",page=1))


def modify(id):

    rating = Rating.query.get(id)

    if request.method == "POST":
        lecture = Lecture.query.get(rating.lecture_id)


        total = int(request.form.get('total'))
        difficulty = int(request.form.get('difficulty'))
        study_time = int(request.form.get('study_time'))
        attendance = int(request.form.get('attendance'))
        grade = int(request.form.get('grade'))
        achievement = int(request.form.get('achievement'))
        content = request.form.get('content')

        lecture.total+= total-rating.total
        lecture.difficulty +=difficulty-rating.difficulty
        lecture.study_time+=study_time-rating.study_time
        lecture.attendance+=attendance-rating.attendance
        lecture.grade+=grade-rating.grade
        lecture.achievement+=achievement-rating.achievement


        rating.total = total
        rating.difficulty = difficulty
        rating.study_time = study_time
        rating.attendance = attendance
        rating.grade = grade
        rating.achievement = achievement
        rating.opinion = content

        db.session.commit()

        return redirect(url_for("my_rating",page=1))


    return render_template("modify_rating.html",lecture=rating)


def evaluate(id):

    lecture = Lecture.query.get(id)

    return render_template("evaluate.html",lecture=lecture)

def ev_input():

    if request.method == "POST":
        id = int(request.form.get('id'))
        lecture = Lecture.query.get(id)

        exist = g.user.rating_user.filter_by(lecture_id=lecture.id).first()

        if exist:
            return jsonify(success=False)

        total = int(request.form.get('total'))
        difficulty = int(request.form.get('difficulty'))
        study_time = int(request.form.get('study_time'))
        attendance = int(request.form.get('attendance'))
        grade = int(request.form.get('grade'))
        achievement = int(request.form.get('achievement'))
        content = request.form.get('content')

        if len(content) < 25:
            return jsonify(success=False)

        rating = Rating(total=total,difficulty=difficulty,study_time=study_time,attendance=attendance,
                        grade=grade,achievement=achievement,lecture_id = lecture.id,user_id=g.user.id,opinion = content)

        lecture.count+=1
        lecture.total+=total
        lecture.difficulty+=difficulty
        lecture.study_time+=study_time
        lecture.attendance+=attendance
        lecture.grade+=grade
        lecture.achievement+=achievement
        g.user.count+=1

        db.session.add(rating)
        db.session.commit()


        return jsonify(success=True)

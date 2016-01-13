# -*- coding: utf-8 -*-
from flask import redirect, url_for, flash, session,render_template,request,jsonify
from apps import app,db
from controller import user,main
from models import User,Lecture,Rating
from sqlalchemy import desc
import math
import logging



@app.route('/')
@app.route('/index')
def index():
    return user.index()

# @app.errorhandler(Exception)
# def page_not_found(e):
#
#     logging.error(e)
#     return render_template("error.html"), 500

# 회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return user.signup()

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    return user.login()

#로그아웃 부분.
@app.route('/logout')
def logout():
    return user.logout()

@app.route('/contact')
def contact():
    return user.contact()

@app.route('/m_pw', methods=['GET', 'POST'])
def modify_password():
    return user.modify_password()

#회원 닉네임 수정
@app.route('/m_nick', methods=['GET', 'POST'])
def modify_nickname():
    return user.modify_nickname()


@app.route('/my_rating/<int:page>', defaults={'page': 1})
@app.route('/my_rating/<int:page>', methods=['GET', 'POST'])
def my_rating(page):

    user = User.query.filter_by(code=session['session_user_code']).first()
    my_rating = user.rating_user.order_by(desc(Rating.joinDATE)).offset((page - 1) * 8).limit(8)
    total = user.rating_user.count()
    calclulate = float(float(total) / 8)
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


    return render_template("my_rating.html",my_rating=my_rating,
                           total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down, page=page)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
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


@app.route('/modify/<int:id>', methods=['GET', 'POST'])
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



@app.route('/search',methods=['GET', 'POST'])
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


@app.route('/search2',methods=['GET', 'POST'])
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


@app.route('/evaluate/<int:id>',methods=['GET', 'POST'])
def evaluate(id):

    if not 'session_user_code' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    lecture = Lecture.query.get(id)


    return render_template("evaluate.html",lecture=lecture)

@app.route('/ev_input',methods=['GET', 'POST'])
def ev_input():

    if request.method == "POST":
        id = int(request.form.get('id'))
        lecture = Lecture.query.get(id)
        user = User.query.filter_by(code = session['session_user_code']).first()

        exist = user.rating_user.filter_by(lecture_id=lecture.id).first()

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
                        grade=grade,achievement=achievement,lecture_id = lecture.id,user_id=user.id,opinion = content)

        lecture.count+=1
        lecture.total+=total
        lecture.difficulty+=difficulty
        lecture.study_time+=study_time
        lecture.attendance+=attendance
        lecture.grade+=grade
        lecture.achievement+=achievement
        user.count+=1

        db.session.add(rating)
        db.session.commit()


        return jsonify(success=True)


@app.route('/detail/<int:id>',methods=['GET', 'POST'])
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

@app.route('/admin',methods=['GET', 'POST'])
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

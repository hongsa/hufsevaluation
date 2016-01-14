# -*- coding: utf-8 -*-
from flask import g, request, redirect, url_for
from apps import app
from controller import user,main,rating
from functools import wraps



#랜딩 페이지
@app.route('/')
@app.route('/index')
def index():

    return user.index()

#에러 페이지
# @app.errorhandler(Exception)
# def page_not_found(e):
#
#     logging.error(e)
#     return render_template("error.html"), 500


#먼저 호출
@app.before_request
def before_request():
    return user.before_request()

#로그인 해야 접속 가능
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('index', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


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

#문의
@app.route('/contact')
@login_required
def contact():
    return user.contact()

#비밀번호 변경
@app.route('/m_pw', methods=['GET', 'POST'])
@login_required
def modify_password():
    return user.modify_password()

#회원 닉네임 수정
@app.route('/m_nick', methods=['GET', 'POST'])
@login_required
def modify_nickname():
    return user.modify_nickname()

#내가 평가한 목록
@app.route('/my_rating/<int:page>', defaults={'page': 1})
@app.route('/my_rating/<int:page>', methods=['GET', 'POST'])
@login_required
def my_rating(page):

    return rating.my_rating(page)

#내가 평가한 것 삭제하기
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):

    return rating.delete(id)

#내가 평가한 것 수정하기
@app.route('/modify/<int:id>', methods=['GET', 'POST'])
@login_required
def modify(id):

    return rating.modify(id)

#강의 평가하기 템플릿
@app.route('/evaluate/<int:id>',methods=['GET', 'POST'])
@login_required
def evaluate(id):

    return rating.evaluate(id)

#강의 점수 입력 ajax
@app.route('/ev_input',methods=['GET', 'POST'])
@login_required
def ev_input():

    return rating.ev_input()


#강의 검색 및 출력 - 강의명, 교수 검색
@app.route('/search',methods=['GET', 'POST'])
@login_required
def search():

    return main.search()

#강의 검색 및 출력 - 구분 검색
@app.route('/search2',methods=['GET', 'POST'])
@login_required
def search2():

    return main.search2()

#세부 강의정보
@app.route('/detail/<int:id>',methods=['GET', 'POST'])
@login_required
def detail(id):

    return main.detail(id)

#관리자 - 강의 입력
@app.route('/admin',methods=['GET', 'POST'])
@login_required
def admin():
    return main.admin()

# -*- coding: utf-8 -*-
import math

from flask import redirect, url_for, render_template,flash, session, request,json,jsonify
from sqlalchemy import desc
from apps import db
from apps.models import Board,BoardReview,User,Like
import logging
import pytz
import datetime

# def get_current_time():
#     return datetime.datetime.now(pytz.timezone('Asia/Seoul'))


def boardList(page):

    board = Board.query.order_by(desc(Board.created)).offset((page - 1) * 15).limit(15)

    total = Board.query.count()
    calclulate = float(float(total) / 15)
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


    return render_template("board.html", board=board,total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,page=page)

def boardWrite():

    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    if request.method == "POST":

        email = session['session_user_email']
        user = User.query.get(email)

        this=Board(
            userEmail = email,
            nickname = user.nickname,
            title = request.form['title'],
            content = request.form['content']
        )

        db.session.add(this)
        db.session.commit()
        return redirect(url_for('boardList',page=1))


    return render_template("boardWrite.html")


def boardDetail(id):

    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    email = session['session_user_email']
    user =User.query.get(email)
    detail = Board.query.get(id)
    detail.click+=1
    db.session.commit()

    review = detail.boardReview_board

    num = Board.query.filter(Board.created > detail.created).order_by(desc(Board.created)).count()+1
    list = math.ceil(float(float(num)/15))

    return render_template("boardDetail.html",detail=detail,review=review, list = int(list))


def boardComment():

    try:
        if request.method == 'POST':
            email = session['session_user_email']
            user= User.query.get(email)
            name=user.nickname
            num = user.numVideo
            if num<50:
                level= 0
            elif 50<=num<100:
                level= 1
            elif 100<=num<200:
                level= 2
            elif 200<=num<400:
                level= 3
            else:
                level= 4
            comment = request.form['comment']
            id = request.form['id']
            thisComment=BoardReview(
                boardId = id,
                userEmail=email,
                content=comment
            )
            #댓글 DB에 저장
            jsonDict = {}
            jsonDict['user']=name
            jsonDict['level']=level
            jsonDict['comments'] = comment
            jsonDict['boardId'] = id

            board = Board.query.get(id)
            board.commentCount+=1
            db.session.add(thisComment)
            db.session.commit()

            return json.dumps(jsonDict)

    except Exception, e:
        print " Occuring Exception. ", e



def boardLike():

    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    id = request.form.get('id')
    board = Board.query.get(id)
    email = session['session_user_email']

    exist = board.like_board.filter_by(userEmail = email).first()

    if exist:
        if exist.evaluate == 0:
            return jsonify(success=True)
        else:
            board.hate-=1
            board.like+=1
            exist.evaluate = 0
            db.session.commit()
            return jsonify(success=True)

    else:
        this = Like(
            userEmail = email,
            boardId = id,
            evaluate =0
        )
        board.like+=1

        db.session.add(this)
        db.session.commit()
        return jsonify(success=True)


def boardHate():

    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))

    id = request.form.get('id')
    board = Board.query.get(id)
    email = session['session_user_email']

    exist = board.like_board.filter_by(userEmail = email).first()

    if exist:
        if exist.evaluate == 1:
            return jsonify(success=True)
        else:
            board.hate+=1
            board.like-=1
            exist.evaluate = 1
            db.session.commit()
            return jsonify(success=True)

    else:
        this = Like(
            userEmail = email,
            boardId = id,
            evaluate =1
        )
        board.hate+=1

        db.session.add(this)
        db.session.commit()
        return jsonify(success=True)




def noticeList(page):

    board = Board.query.filter_by(category=1).order_by(desc(Board.created)).offset((page - 1) * 15).limit(15)

    total = Board.query.filter_by(category=1).count()
    calclulate = float(float(total) / 15)
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


    return render_template("notice.html", board=board,total_page=range(1+(10*(int(a)-1)), int(total_page+1)), up = up, down = down,page=page)

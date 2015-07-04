# -*- coding: utf-8 -*-
from flask import redirect, url_for, flash, session,render_template
from google.appengine.api import urlfetch
from apps import app,db
from apps.controller import video
from models import User,Actor,Video
from controller import user,actor,newActor,newVideo,newVideo2,search,admin,collection,star,bookmark,detail,board,main
import recommendation,recommendation2
import readImage
import logging
import json
import time
from google.appengine.runtime import DeadlineExceededError
from google.appengine.api import urlfetch
from sqlalchemy import desc
import math
# userController에서 관리하는 부분 시작

# def getMicrotime():
#     return time.time()
#
# def timeLogger(message, startTime, endTime):
#     sMessage = message + " :: " + str( endTime - startTime )
#     logging.error( sMessage)

@app.route('/')
@app.route('/index')
def index():

    return user.index()
    # return render_template("serverout.html")

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

# 회원 비밀번호 수정
@app.route('/m_pw', methods=['GET', 'POST'])
def modify_password():
    return user.modify_password()

#회원 닉네임 수정
@app.route('/m_nick', methods=['GET', 'POST'])
def modify_nickname():
    return user.modify_nickname()

@app.route('/contact', methods=['GET','POST'])
def contact():
    return user.contact()
# userController 관리부분 끝


#메인페이지!!
@app.route('/main', methods=['GET','POST'])
def main_page():
    return main.main_page()

@app.route('/r_actor', methods=['GET','POST'])
def review_actor():
    return main.review_actor()

@app.route('/r_video', methods=['GET','POST'])
def review_video():
    return main.review_video()

@app.route('/s_actor', methods=['GET','POST'])
def star_actor():
    return main.star_actor()

@app.route('/s_video', methods=['GET','POST'])
def star_video():
    return main.star_video()




#배우 평가(actorController)
@app.route('/actor_main', methods=['GET', 'POST'])
def actor_main():
    # return render_template("serverout.html")
    return actor.actor_main()

@app.route('/show2/<key>', methods=['GET', 'POST'])
def show2(key):
    return actor.show2(key)

@app.route('/a_category/<path:name>', defaults={'page': 1})
@app.route('/a_category/<path:name>/<int:page>', methods=['GET', 'POST'])
def actor_category(name, page):
    return actor.actor_category(name,page)

@app.route('/a_category2/<path:name>', defaults={'page': 1})
@app.route('/a_category2/<path:name>/<int:page>', methods=['GET', 'POST'])
def actor_category2(name, page):
    return actor.actor_category2(name,page)

#배우 평가(actorController) 끝



#영상 평가(videoController)
@app.route('/video_main', methods=['GET', 'POST'])
def video_main():

    # return render_template("serverout.html")
    return video.video_main()

@app.route('/show1/<key>', methods=['GET', 'POST'])
def show1(key):
    return video.show1(key)

@app.route('/v_category/<path:name>', defaults={'page': 1})
@app.route('/v_category/<path:name>/<int:page>', methods=['GET', 'POST'])
def video_category(name, page):
    return video.video_category(name,page)

@app.route('/v_category2/<path:name>', defaults={'page': 1})
@app.route('/v_category2/<path:name>/<int:page>', methods=['GET', 'POST'])
def video_category2(name, page):
    return video.video_category2(name,page)
#영상 평가(videoController) 끝




#신작평가(newActorController, newVideoController)
@app.route('/n_actor/<int:name>/<int:page>', methods=['GET', 'POST'])
@app.route('/n_actor/<int:name>', defaults={'page': 1}, methods=['GET','POST'])
def new_actor(name, page):
    return newActor.new_actor(name,page)

@app.route('/n_video/<path:name>', defaults={'page': 1})
@app.route('/n_video/<path:name>/<int:page>', methods=['GET', 'POST'])
def new_video(name, page):
    return newVideo.new_video(name,page)

@app.route('/n_video2/<int:name>', defaults={'page': 1})
@app.route('/n_video2/<int:name>/<int:page>', methods=['GET', 'POST'])
def new_video2(name, page):
    return newVideo2.new_video2(name,page)

#신작평가(newActorController, newVideoController) 끝



#검색(seachController)
#디비검색
@app.route('/db_search', methods=['GET', 'POST'])
def db_search(searching_word):
    return search.db_search(searching_word)

#구글검색
@app.route('/g_search', methods=['GET', 'POST'])
def g_search():
    return search.g_search()
#검색(seachController) 끝


#관리자(adminController)
@app.route('/admin', methods=['GET', 'POST'])
def admin_main():
    return admin.admin_main()

@app.route('/admin_actor', methods=['GET', 'POST'])
def admin_actor():
    return admin.admin_actor()

@app.route('/admin_actor_check', methods=['GET', 'POST'])
def admin_actor_check():
    return admin.admin_actor_check()

@app.route('/admin_video', methods=['GET', 'POST'])
def admin_video():
    return admin.admin_video()

@app.route('/admin_video_check', methods=['GET', 'POST'])
def admin_video_check():
    return admin.admin_video_check()

@app.route('/admin_connect', methods=['GET', 'POST'])
def admin_connect():
    return admin.admin_connect()

@app.route('/admin_edit', methods=['GET', 'POST'])
def admin_edit():
    return admin.admin_edit()

# @app.route('/admin_a_img', methods=['GET', 'POST'])
# def admin_a_img():
#     return admin.admin_a_img()
#
# @app.route('/admin_v_img', methods=['GET', 'POST'])
# def admin_v_img():
#     return admin.admin_v_img()



#관리자(adminController) 끝



#콜렉션(collectionController)
@app.route('/a_collection_b/<int:page>', defaults={'page': 1})
@app.route('/a_collection_b/<int:page>', methods=['GET', 'POST'])
def actor_collection_bookmark(page):
    return collection.actor_collection_bookmark(page)

@app.route('/a_collection_r/<int:page>', defaults={'page': 1})
@app.route('/a_collection_r/<int:page>', methods=['GET', 'POST'])
def actor_collection_rating(page):
    return collection.actor_collection_rating(page)

@app.route('/v_collection_b/<int:page>', defaults={'page': 1})
@app.route('/v_collection_b/<int:page>', methods=['GET', 'POST'])
def video_collection_bookmark(page):
    return collection.video_collection_bookmark(page)

@app.route('/v_collection_r/<int:page>', defaults={'page': 1})
@app.route('/v_collection_r/<int:page>', methods=['GET', 'POST'])
def video_collection_rating(page):
    return collection.video_collection_rating(page)
#콜렉션(collectionController) 끝



#별점(star)
@app.route('/v_save_star', methods=['GET', 'POST'])
def video_save_star():
    return star.video_save_star()

@app.route('/a_save_star', methods=['GET', 'POST'])
def actor_save_star():
    return star.actor_save_star()
# 별점(star) 끝


#북마크(bookmark)
@app.route('/a_bookmark', methods=['GET', 'POST'])
def actor_bookmark():
    return bookmark.actor_bookmark()

@app.route('/v_bookmark', methods=['GET', 'POST'])
def video_bookmark():
    return bookmark.video_bookmark()
#북마크(bookmark) 끝



# 배우 디테일
@app.route('/actorDetail/<string:name>', methods=['GET', 'POST'])
def actorDetail(name):
    return detail.actorDetail(name)

#댓글입력
@app.route('/actor/comment', methods=['POST'])
def actor_comment():
    return detail.actor_comment()
#댓글삭제
@app.route('/a_comment/delete/<int:id>', methods=['GET','POST'])
def a_comment_delete(id):
    return detail.a_comment_delete(id)

@app.route('/a_comment_rows', methods=['GET','POST'])
def a_comment_rows():
    return detail.a_comment_rows()

@app.route('/v_comment_rows', methods=['GET','POST'])
def v_comment_rows():
    return detail.v_comment_rows()




#영상 디테일
@app.route('/videoDetail/<string:name>', methods=['GET', 'POST'])
def videoDetail(name):
    return detail.videoDetail(name)

#댓글입력
@app.route('/video/comment', methods=['POST'])
def video_comment():
    return detail.video_comment()
#댓글삭제
@app.route('/v_comment/delete/<int:id>', methods=['GET','POST'])
def v_comment_delete(id):
    return detail.v_comment_delete(id)


# 게시판
@app.route('/board/<int:page>')
@app.route('/board<int:page>',methods=['GET', 'POST'])
def boardList(page):
    return board.boardList(page)

@app.route('/b_write',methods=['GET', 'POST'])
def boardWrite():
    return board.boardWrite()

@app.route('/b_detail/<int:id>',methods=['GET', 'POST'])
def boardDetail(id):
    return board.boardDetail(id)

@app.route('/b_comment',methods=['GET', 'POST'])
def boardComment():
    return board.boardComment()

@app.route('/b_like',methods=['GET', 'POST'])
def boardLike():
    return board.boardLike()

@app.route('/b_hate',methods=['GET', 'POST'])
def boardHate():
    return board.boardHate()

@app.route('/notice/<int:page>')
@app.route('/notice/<int:page>',methods=['GET', 'POST'])
def noticeList(page):
    return board.noticeList(page)




# 영상 추천기능
@app.route('/recommendation',methods=['GET','POST'])
def recommend():
    #로그인 안돼있으면 튕기는 부분
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))
    email = session['session_user_email']
    cUser = User.query.get(email)
    # count = len(cUser.ratings())
    countVideo = cUser.numVideo
    # logging.error(count)
    rList = False
    # success=""
    # 추천 수가 부족할 경우 추천 알고리즘 안돌림
    if countVideo < 24:
        return render_template("recommendation.html",count=countVideo, rList=rList)
    else:
        logging.error("1")
        if cUser.prefsVideo == None:
            logging.error("2")
            # success = False
            # try:
            list = recommendation2.getSoulmate(recommendation2.makeVideoRowData(),email,n=5)
            # logging.error(list)
            logging.error("3")
            a = json.dumps(list)
            cUser.prefsVideo = a
            db.session.commit()
            # success = True
            # except:pass
            # if success == True:
            #     logging.error("4")
            #     try:
            # prefs = json.loads(cUser.prefsVideo)
            rList = recommendation2.getRecommendations(recommendation2.makePrefs(list),email,similarity=recommendation2.simPearson)
                # except:pass
        else:
            # try:
            logging.error("4")
            prefs = json.loads(cUser.prefsVideo)
            rList = recommendation2.getRecommendations(recommendation2.makePrefs(prefs),email,similarity=recommendation2.simPearson)
            # except:pass

        return render_template('recommendation.html', rList=rList,count=countVideo)
        # return 'well done'

# 배우 추천기능
@app.route('/recomm',methods=['GET','POST'])
def recommend2():
    #로그인 안돼있으면 튕기는 부분
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))
    email = session['session_user_email']
    cUser = User.query.get(email)
    # count = len(cUser.aRatings())
    countActor = cUser.numActor
    # logging.error(count)
    rList = False
    # success=""
    # 추천 수가 부족할 경우 추천 알고리즘 안돌림
    if countActor<24:
        return render_template("recomm.html",count=countActor,rList=rList)
    else:
        logging.error("1")
        if cUser.prefsActor ==None:
            logging.error("2")
            # success = False
            # _x = getMicrotime()
            # try:
            list = recommendation2.getSoulmate(recommendation2.makeActorRowData(),email,n=5)
            logging.error("3")
            # logging.error(list)
            a = json.dumps(list)
            cUser.prefsActor = a
            db.session.commit()
            # success = True
            # except:pass
            # if success == True:
            #     try:
            # prefs = json.loads(cUser.prefsActor)
            rList = recommendation2.getRecommendations(recommendation2.makePrefsActor(list),email,similarity=recommendation2.simPearson)
                # except:pass
            # _y = getMicrotime()
            # timeLogger("firstTry", _x, _y)
        else:
            # try:

                # _s = getMicrotime()
            logging.error("4")
            prefs = json.loads(cUser.prefsActor)
            rList = recommendation2.getRecommendations(recommendation2.makePrefsActor(prefs),email,similarity=recommendation2.simPearson)
                # _e = getMicrotime()
                # timeLogger("rList", _s, _e)
            # except:pass
        # _s = getMicrotime()
        # rList = recommendation.getRecommendations(recommendation.makeActorRowData(),email,similarity=recommendation.simPearson)
        # _e = getMicrotime()
        # timeLogger("rList", _s, _e)
        return render_template('recomm.html', rList=rList, count=countActor)
    # return 'well done'


#전설이 시작되는 부분
#영상평가가 유사한 친구들을 추가하는 부분.
@app.route('/backmirror1/<int:pag>',defaults={'page':1})
@app.route('/backmirror1/<int:pag>',methods=['GET', 'POST'])
def test1(pag):
    oUser = User.query.filter(User.numVideo>24).order_by(desc(User.numVideo)).offset((pag-1)*20).limit(20)

    if not 'oVideo' in session:
        session['oVideo'] = recommendation2.makeVideoRowData()

    oVideo = session['oVideo']

    for each in oUser:
        try:
            list = recommendation2.getSoulmate(oVideo,each.email,n=5)
            a = json.dumps(list)
            each.prefsVideo = a
            db.session.commit()
            # logging.error(str(each.email)+"'s list" + a)
        except:
            logging.error(str(each.email)+"'s error")

    if pag>20:
        return 'done'
    else:
        logging.error("now"+pag)
        return redirect(url_for('test1', pag=pag+1))
#
# 배우평가가 유사한 친구들을 추가하는 부분.
@app.route('/backmirror2/<int:page>',defaults={'page':1})
@app.route('/backmirror2/<int:page>',methods=['GET', 'POST'])
def test2(page):
    #
    oUser = User.query.filter(User.numActor>24).order_by(desc(User.numActor)).offset((page-1)*20).limit(20)
    #
    if not 'oActor' in session:
        session['oActor'] = recommendation2.makeActorRowData()
    oActor = session['oActor']

    for each in oUser:
        try:
            list = recommendation2.getSoulmate(oActor,each.email,n=5)
            a = json.dumps(list)
            each.prefsActor = a
            db.session.commit()
            # logging.error(str(each.email)+"'s list" + a)
        except:
            logging.error(str(each.email)+"'s error")

    if page>20:
        return 'done'
    else:
        logging.error("now"+page)
        return redirect(url_for('test2', page=page+1))
# 유사 영상 찾는 함수
@app.route('/simvideo/<int:page>',defaults={'page':1})
@app.route('/simvideo/<int:page>',methods=['GET', 'POST'])
def simvideos(page):

    # if not 'oDict' in session:
    oDict = recommendation2.simVideoPrefs()

    # oDict = session['oDict']
    videos = Video.query.filter(Video.count>4).order_by(desc(Video.count)).offset((page - 1) * 50).limit(30)
    c = 0
    for each in videos:
        # 큰 데이터 세트를 위해 진척 상태를 갱신
        #
        # 각 항목과 가장 유사한 항목들을 구함
        list = []
        success = False
        try:
            list = recommendation2.getSoulmate(oDict,each.name,n=5,similarity=recommendation2.simPearson)
            # logging.error(list)
            success = True
        except: logging.error(str(each.name)+"'s error")
        if success:
            logging.error(str(each.name)+"'s list")
            # logging.error(list)
            each.prefs = json.dumps(list)
            db.session.commit()

        # a = json.dumps(list)
        # each.prefs = a
        # db.session.commit()

    if page>50:
        return 'done'
    else:
        logging.error("now"+str(page))
        return redirect(url_for('simvideos', page=page+1))
    # return 'done'
#
# 유사 배우 찾는 함수
@app.route('/simactor/<int:page>',defaults={'page':1})
@app.route('/simactor/<int:page>',methods=['GET', 'POST'])
def simactors(page):
    # if not 'oItem' in session:
    oItem = recommendation2.simActorPrefs()

    actors = Actor.query.filter(Actor.count>4).order_by(desc(Actor.count)).offset((page - 1) * 30).limit(30)
    # oItem = session['oItem']

    c = 0
    for each in actors:

        # 각 항목과 가장 유사한 항목들을 구함
        # _s = getMicrotime()
        list = []
        success = False
        try:
            list = recommendation2.getSoulmate(oItem,each.name,n=5,similarity=recommendation2.simPearson)
            logging.error(list)
            success=True

        except: logging.error(str(each.name)+"'s error")

        if success:
            logging.error(str(each.name)+"'s list")
            # logging.error(list)
            each.prefs = json.dumps(list)
            db.session.commit()
        # _e = getMicrotime()
        #
        # timeLogger("list", _s, _e)

        # _s = getMicrotime()
        # a = json.dumps(list)
        # each.prefs = a
        # db.session.commit()
        # _e = getMicrotime()
        # timeLogger("commit", _s, _e)
    if page > 50:
        return 'done'
    else:
        logging.error("now"+str(page))
        return redirect(url_for('simactors',page=page+1))
    # return  'done'
#



#이제 필요없음


#
# @app.route('/sex/<int:page>',defaults={'page':1})
# @app.route('/sex/<int:page>',methods=['GET', 'POST'])
# def numActor(page):
#     a = User.query.order_by(desc(User.joinDATE)).offset((page - 1) * 100).limit(100)
#     for each in a:
#         if each.numVideo:
#             pass
#         else:
#             each.numActor = len(each.aRatings())
#             db.session.commit()
#     if page == 310:
#         return 'done'
#     return redirect(url_for("numActor",page=page+1))
#
# @app.route('/bozi/<int:page>',defaults={'page':1})
# @app.route('/bozi/<int:page>',methods=['GET', 'POST'])
# def numVideo(page):
#     # 배우랑 키 가져오기
#     a = User.query.order_by(desc(User.joinDATE)).offset((page - 1) * 100).limit(100)
#     for each in a:
#         if not each.numVideo:
#             each.numVideo = len(each.ratings())
#             db.session.commit()
#         else:
#             pass
#     if page==310:
#         return 'done'
#     return redirect(url_for("numVideo",page=page+1))
#
#
#
#

# -*- coding: utf-8 -*-
from flask import redirect, url_for, flash, session,render_template
from apps import app
from apps.controller import video
from models import User
from controller import user,actor,newActor,newVideo,search,admin,collection,star,bookmark,detail
import recommendation

# userController에서 관리하는 부분 시작
@app.route('/')
@app.route('/index')
def index():
    return user.index()

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



#배우 평가(actorController)
@app.route('/actor_main', methods=['GET', 'POST'])
def actor_main():
    return actor.actor_main()

@app.route('/show2/<key>', methods=['GET', 'POST'])
def show2(key):
    return actor.show2(key)

@app.route('/a_category/<path:name>', defaults={'page': 1})
@app.route('/a_category/<path:name>/<int:page>', methods=['GET', 'POST'])
def actor_category(name, page):
    return actor.actor_category(name,page)
#배우 평가(actorController) 끝



#영상 평가(videoController)
@app.route('/video_main', methods=['GET', 'POST'])
def video_main():
    return video.video_main()

@app.route('/show1/<key>', methods=['GET', 'POST'])
def show1(key):
    return video.show1(key)

@app.route('/v_category/<path:name>', defaults={'page': 1})
@app.route('/v_category/<path:name>/<int:page>', methods=['GET', 'POST'])
def video_category(name, page):
    return video.video_category(name,page)
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


#영상 디테일
@app.route('/videoDetail/<string:name>', methods=['GET', 'POST'])
def videoDetail(name):
    return detail.videoDetail(name)

#댓글입력
@app.route('/video/comment', methods=['POST'])
def video_comment():
    return detail.video_comment()



# 추천기능
@app.route('/recommendation',methods=['GET','POST'])
def recommend():
    #로그인 안돼있으면 튕기는 부분
    if not 'session_user_email' in session:
        flash(u"로그인 되어있지 않습니다.", "error")
        return redirect(url_for('index'))
    email = session['session_user_email']
    cUser = User.query.get(email)
    # 추천 수가 부족할 경우 추천 알고리즘 안돌림
    if len(cUser.ratings())<=25:
        return '평가를 더 하셔야 합니다.'
    # logging.error(dict)
    # logging.error(recommendation.getRecommendations(dict,cUser.nickname,similarity=recommendation.simPearson))
    # 완성된 표본과 유저정보(닉네임)를 알고리즘 함수에 제출
    # logging.error(recommendation.getRecommendations(dict,cUser.nickname,similarity=recommendation.simPearson)
    rList = recommendation.getRecommendations(recommendation.makePrefs(),cUser.nickname,similarity=recommendation.simPearson)

    # list = [1,2,3]
    return render_template('recommendation.html', rList=rList)
    # return 'well done'

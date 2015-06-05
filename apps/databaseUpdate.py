# # -*- coding: utf-8 -*-
# from flask import redirect, url_for, flash, session,render_template
# from google.appengine.api import urlfetch
# from apps import app,db
# from apps.controller import video
# from apps.models import Actor,User
# import logging
#
#
# def test1():
#     oUser = User.query.filter(User.numVideo>24).all()
#     user=[]
#     for each in oUser:
#         user.append(each.email)
#
#     print user
#
# test1()
#
# userVideo=[u'baybay223@naver.com', u'efjfskd@haha.com', u'jejd916@naver.com', u'llbeezer@naver.com', u'nike_mania@naver.com', u'rogurrl@hanmail.net', u'skrkdhzm@naver.com', u'stellius@naver.com', u'stone1202@naver.com', u'tanggo24@naver.com', u'tkdrl3411@naver.com', u'zero19090@naver.com', u'aaab@aaa.com', u'chldudwo22@naver.com', u'dudxo@naver.com', u'ekradone@gmail.com', u'hvitaminc@naver.com', u'idboos@nate.com', u'jjh5645@naver.com', u'jobyejin45@daum.net', u'kairstrip@hanmail.net', u'kjha1020@naver.com', u'korea1212@naver.com', u'kwosu@hanmail.net', u'lanowar@nate.com', u'lelouch0s@nate.com', u'ljb1306@gmail.com', u'mbj711@naver.com', u'mulgam99@nate.com', u'pepsl81521@gmail.com', u'qkrfkdpahd@naver.com', u'qkrwhdgu1@naver.com', u'ruker1024@gmail.com', u'secretter@gmail.com', u'serene15@naver.com', u'sic5192@naver.com', u'souloforder@gmail.com', u'wjddo@naver.com', u'wkdwhdtnjjs@naver.com', u'yunjinnim@gmail.com', u'zhzhvkavka1@hanmail.net', u'112@naver.com', u'alwkdkemf@naver.com', u'audrl132@naver.com', u'brownanonymous1@gmail.com', u'c.impressive@gmail.com', u'ddd43545@naver.com', u'dldudgns5979@naver.com', u'ehowl123@gmail.com', u'freemutal36@naver.com', u'ghostinfate@naver.com', u'hakingtg@gmail.com', u'ohmohm@naver.com', u'orcen@naver.com', u'overslip@hotmail.com', u'ppp9999@naver.com', u'romiromiromi98@gmail.com', u'saga0001@naver.com', u'seonggn@naver.com', u'sleipnir@korea.com', u'ss@ss.com', u'sw3279@sayclub.com', u'ttl321@nate.com', u'yamyami2000@naver.com', u'djdhehdn@sjdjf.com', u'dnjsdyd1987@gmail.com', u'dongsoo37@naver.com', u'elegy150@naver.com', u'gamesu@nate.com', u'hong1113@naver.com', u'ijh1027@gmail.com', u'iminchaos@gmail.com', u'jike33@naver.com', u'jjunggul@naver.com', u'kastrok@naver.com', u'kkdkkd99@naver.com', u'likeingsky@naver.com', u'noisy100@gmail.com', u'qkrqldtjqj@naver.com', u'qntkrka@naver.com', u'roy1241@naver.com', u'shyun316@nate.com', u'syhj012486@gmail.com', u'whfmrk@naver.com', u'yhl0203@nate.com', u'aassdd@naver.com', u'awesome9045@naver.com', u'clc0089@naver.com', u'csppaa403@naver.com', u'hyj2000-y2k@hanmail.net', u'kdy2012@naver.com', u'pyb2938@nate.com', u'sasung1@naver.com', u'whiteloa@hotmail.com', u'wldnjs5548@naver.com', u'ypkbus@gmail.com', u'52452412@naver.com', u'jjyh2530', u'khai506@naver.com', u'leetw4@naver.com', u'money619@naver.com', u'to.remember@hanmail.net', u'babonot@hanmail.com', u'duswnd25@gmail.com', u'kms3024@naver.com', u'obh9988@naver.com', u'ok@bold.kr', u'qoochang@naver.com', u'rlagkswnd28@gmail.com', u'scvhss2@naver.com', u'tmdruf830@naver.com', u'ubollet@naver.com', u'wolf269@nate.com', u'boxer_stars@naver.com', u'dynamicjo1@gmail.com', u'gorapasub@gmail.com', u'ppwwee@naver.com', u'yumras@hotmail.com', u'database1942@gmail.com', u'dongyoo486@gmail.com', u'jurapj@naver.com', u'marco_@naver.com', u'nobjob@naver.com', u'qq2wr@lee.sin', u'shin8712@gmail.com', u'yayaya@naver.com', u'aaa04751@naver.com', u'anjea123@naver.com', u'liquidelixir@gmail.com', u'neopmank@gmail.com', u'skylove1290@naver.com', u'alchem20@naver.com', u'keira711@gmail.com', u'mog5113@nate.com', u'monsters0479@hanmail.net', u'pmskku@naver.com', u'test1@test.com', u'bw1213@gmail.com', u'kst6250@naver.com', u'loveof32@naver.com', u'asdf13@lycos.co.kr', u'godgod826@naver.com', u'money5669@naver.com', u'rj7568@naver.com', u'sadsalsa00@hotmail.com', u'zzim1135@naver.com', u'123philip@naver.com', u'bbm7531@gmail.com', u'dlfghldyd@naver.com', u'fl.armso@gmail.com', u'kjh64481@nate.com', u'puremerit74@gmail.com', u'vigston@naver.com', u'kickass9090@gmail.com', u'namodori@gmail.com', u'qnpfr1845@naver.com', u'carpediem1538@hotmail.com', u'dkdldhdodh2@naver.com', u'gangnam12@gmail.com', u'sssss@naver.com', u'ppapper@gmail.com', u'zg021@naver.com', u'goku@naver.com', u'djabdl@naver.com', u'kdksay@hanmail.com', u'tigers@naver.com', u'dandydj@naver.com', u'story7486@gmail.com', u'ufoscw@naver.com', u'yeum125@naver.com', u'dnwls9446@naver.com', u'conichiwa@naver.com', u's1ee@hanmail.net', u'darkmash11@gmail.com', u'dnokok@naver.com', u'postscotch@outlook.com', u'test6060@nate.com', u'jinyeong88@hanmail.net', u'bercerke@naver.com', u'rmsmemfm11@gmail.com', u'leej112@naver.com', u'bong.al@gmail.com', u'kimsk53@naver.com', u'qwerty@gmail.com', u'scvhss@naver.com', u'sinjung525']




    # oVideo = recommendation2.makeVideoRowData()

    # for each in oUser:
    #     try:
    #         list = recommendation2.getSoulmate(oVideo,each.email,n=5)
    #         a = json.dumps(list)
    #         each.prefsVideo = a
    #         db.session.commit()
        # except:
        #     logging.error(str(each.email)+"'s error")
    #
# 배우평가가 유사한 친구들을 추가하는 부분.
# def test2(page):
#     #
#     oUser = User.query.filter(User.numActor>24).order_by(desc(User.numActor)).offset((page-1)*20).limit(20)
#     #
#     if not 'oActor' in session:
#         session['oActor'] = recommendation2.makeActorRowData()
#     oActor = session['oActor']
#
#     for each in oUser:
#         try:
#             list = recommendation2.getSoulmate(oActor,each.email,n=5)
#             a = json.dumps(list)
#             each.prefsActor = a
#             db.session.commit()
#             # logging.error(str(each.email)+"'s list" + a)
#         except:
#             logging.error(str(each.email)+"'s error")
#
#     if page>20:
#         return 'done'
#     else:
#         logging.error("now"+page)
#         return redirect(url_for('test2', page=page+1))
# # 유사 영상 찾는 함수
# def simvideos(page):
#
#     # if not 'oDict' in session:
#     oDict = recommendation2.simVideoPrefs()
#
#     # oDict = session['oDict']
#     videos = Video.query.filter(Video.count>4).order_by(desc(Video.count)).offset((page - 1) * 50).limit(30)
#     c = 0
#     for each in videos:
#         # 큰 데이터 세트를 위해 진척 상태를 갱신
#         #
#         # 각 항목과 가장 유사한 항목들을 구함
#         list = []
#         success = False
#         try:
#             list = recommendation2.getSoulmate(oDict,each.name,n=5,similarity=recommendation2.simPearson)
#             # logging.error(list)
#             success = True
#         except: logging.error(str(each.name)+"'s error")
#         if success:
#             logging.error(str(each.name)+"'s list")
#             # logging.error(list)
#             each.prefs = json.dumps(list)
#             db.session.commit()
#
#         # a = json.dumps(list)
#         # each.prefs = a
#         # db.session.commit()
#
#     if page>50:
#         return 'done'
#     else:
#         logging.error("now"+str(page))
#         return redirect(url_for('simvideos', page=page+1))
#     # return 'done'
# #
# # 유사 배우 찾는 함수
# def simactors(page):
#     # if not 'oItem' in session:
#     oItem = recommendation2.simActorPrefs()
#
#     actors = Actor.query.filter(Actor.count>4).order_by(desc(Actor.count)).offset((page - 1) * 30).limit(30)
#     # oItem = session['oItem']
#
#     c = 0
#     for each in actors:
#
#         # 각 항목과 가장 유사한 항목들을 구함
#         # _s = getMicrotime()
#         list = []
#         success = False
#         try:
#             list = recommendation2.getSoulmate(oItem,each.name,n=5,similarity=recommendation2.simPearson)
#             logging.error(list)
#             success=True
#
#         except: logging.error(str(each.name)+"'s error")
#
#         if success:
#             logging.error(str(each.name)+"'s list")
#             # logging.error(list)
#             each.prefs = json.dumps(list)
#             db.session.commit()
#         # _e = getMicrotime()
#         #
#         # timeLogger("list", _s, _e)
#
#         # _s = getMicrotime()
#         # a = json.dumps(list)
#         # each.prefs = a
#         # db.session.commit()
#         # _e = getMicrotime()
#         # timeLogger("commit", _s, _e)
#     if page > 50:
#         return 'done'
#     else:
#         logging.error("now"+str(page))
#         return redirect(url_for('simactors',page=page+1))

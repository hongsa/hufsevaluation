# 키 수정하기 크롤링
# from flask import Flask, render_template
# from apps import app
# from bs4 import BeautifulSoup
# import urllib2
# import re
# import logging

# from apps import db
# #
# @app.route('/crawling/<int:page>',defaults={'page':1})
# @app.route('/crawling/<int:page>',methods=['GET', 'POST'])
# def crawling(page):
#     # 배우랑 키 가져오기
#     a = Actor.query.order_by(desc(Actor.average)).offset((page - 1) * 20).limit(20)
#     actor = []
#     for i in a:
#         actor.append(i.name.replace(" ","") )
#
#     final=[]
#     for each in actor:
#
#         url = "http://hentaku.tistory.com/entry/" + str(each)
#         try:
#             source = urllib2.urlopen( url ).read()
#         except:
#             continue
#         soup = BeautifulSoup( source ,from_encoding="utf-8")
#
#         list=""
#         for total in soup.find_all("div","avstar_info_b"):
#             list=total.text
#         # logging.error(list)
#
#         # final = []
#         name = re.compile(u"[^ \u3131-\u3163\uac00-\ud7a3]+")
#         height = re.compile("[1][4-8][0-9]")
#
#         result1 = name.sub("",list)
#         result2 = height.findall(list)
#         str2 = ''.join(result2)
#
#         final.append(dict(name=result1,value=str2))
#
#
#         logging.error(final)
#         # logging.error(result1)
#         # logging.error(result2)
#
#
#     for each in final:
#         actor = Actor.query.get(each['name'])
#         if actor == None:
#             continue
#
#         if each['value'] =="" :
#             actor.height = 155
#             each['value'] = 155
#         else:
#             actor.height = int(each['value'])
#
#         if int(each['value']) <=154:
#             actor.category ="1"
#         elif 155 <=int(each['value']) <=159:
#             actor.category="2"
#         elif 160 <=int(each['value']) <=164:
#             actor.category="3"
#         elif int(each['value']) >=165:
#             actor.category="4"
#         else:
#             actor.category="2"
#         flash(u"저장 완료")
#         db.session.commit()
#
#     return render_template("crawl.html", final=final)

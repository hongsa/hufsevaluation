# # coding=utf-8
# from threading import Thread
# from flask import render_template
# from flask_mail import Message
# from .. import mail
#
# def toSendEmail(to, userKey):
#     msg = Message(
#         '비밀번호변경',
#         sender= u'jikbakguri.com@google.com',
#         recipients=[to])
#     msg.body = u'아래 링크에서 비밀번호를 변경해주세요. \n http://www.jikbakguri.com/passwdReset/'+userKey
#     print msg
#     mail.send(msg)
#
#
#

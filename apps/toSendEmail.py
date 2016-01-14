# # coding=utf-8
# from flask import Flask
# from flask_mail import Mail, Message
#
# app = Flask(__name__)
# mail = Mail(app)
#
#
# app.config.update(
#     DEBUG = True,
#     MAIL_SERVER='smtp.googlemail.com',
#     MAIL_PORT=465,
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME='hufsevaluate',
#     MAIL_PASSWORD='tktmdrmawltmdghl!'
# )
#
# mail = Mail(app)
#
# emailAddr = 'scvhss@naver.com'
#
# def index():
#     msg = Message(
#         '비밀번호변경',
#         sender='hufsevaluate@gmail.com',
#         recipients=[emailAddr])
#     mail.send(msg)
#     return 'Sent'
#
#
# if __name__ == '__main__':
#     app.run()
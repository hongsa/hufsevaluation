# # -*- coding: utf-8 -*-
# from flask import redirect, url_for, render_template, request, flash, session,g
# from apps import db
# from werkzeug.security import generate_password_hash, check_password_hash
# from apps.models import User
# from apps import forms
# from itsdangerous import URLSafeTimedSerializer
# from . import sendEmail
# import logging
#
#
#
# def passwdEamilReset():
#     form = forms.passwdResetEmailForm()
#
#     if request.method == "POST":
#         if form.validate_on_submit():
#             emailAddr = form.email.data
#             user = User.query.get(emailAddr)
#             if user is not None :
#                 passwdResetEmailSend(emailAddr)
#                 flash(u"해당 이메일로 접속하셔서 링크를 클릭해주세요.","push")
#             if user is None :
#                 flash(u"등록되지 않은 이메일 입니다.","push")
#     return render_template("passwdReset.html", form=form)
#
#
# def passwdResetEmailSend(emailAddr):
#     key = URLSafeTimedSerializer('AOAzzang!!!hahahaha')
#     userKey = key.dumps(emailAddr)
#     try:
#         sendEmail.toSendEmail(emailAddr, userKey)
#     except:
#         pass
#     pass
#
# def passwdReset(token):
#     form = forms.passwdResetConfirm()
#
#     if request.method == "POST":
#         form = forms.passwdResetConfirm()
#         key = URLSafeTimedSerializer('AOAzzang!!!hahahaha')
#         emailAddr = key.loads(token)
#         user = User.query.get(emailAddr)
#         if form.validate_on_submit():
#             try:
#                 passwd = generate_password_hash(form.password.data)
#                 user.password = passwd
#                 db.session.commit()
#                 flash(u"변경 완료되었습니다.", "error")
#             except:
#                 print 'update error'
#         return redirect(url_for('main_page'))
#     return render_template("passwdResetUser.html", form=form)
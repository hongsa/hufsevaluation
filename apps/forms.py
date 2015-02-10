# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField,SelectField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class JoinForm(Form):
    email = EmailField(
        u'이메일주소',
        [validators.data_required(u'이메일을 입력해주세요.')],
        description={'placeholder': u'등록하실 메일주소!'}
    )
    password = PasswordField(
        u'비밀번호',
        [validators.data_required(u'비밀번호를 입력해주세요.'),
         validators.EqualTo('confirm_password', message=u'비밀번호가 일치하지 않습니다!')],
        description={'placeholder': u'비밀번호!'}
    )
    confirm_password = PasswordField(
        u'비밀번호 확인',
        [validators.data_required(u'패스워드를 한번 더 입력하세요.')],
        description={'placeholder': u'한번 더!'}
    )
    nickname = StringField(
        u'닉네임',
        [validators.data_required(u'닉네임을 입력해주세요.(최대 6자)'),validators.length(max=7, message=u"최대 6자이내로 정해주세요.")],
        description={'placeholder': u'원하시는 닉네임!(최대 6자)'}
    )
    sex = SelectField(
        u'성별', coerce=int, choices=[(0,u'남자'),(1,u'여자')]
    )


class LoginForm(Form):
    email = EmailField(
        u'이메일주소',
        [validators.data_required(u'이메일을 입력해주세요.')],
        description={'placeholder': u'등록했던 이메일주소!'}
    )
    password = PasswordField(
        u'비밀번호',
        [validators.data_required(u'비밀번호를 입력해주세요.')],
        description={'placeholder': u'비밀번호!'}
    )
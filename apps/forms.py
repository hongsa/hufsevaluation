# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField,SelectField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class JoinForm(Form):
    code = StringField(
        u'외대 학번',
        [validators.data_required(u'학번을 입력해주세요.')],
        description={'placeholder': u'자신의 학번을 정확히 입력해주세요.'}
    )

    # email = StringField(
    #     u'외대 이메일',
    #     [validators.data_required(u'뒤는 무조건 @hufs.ac.kr')],
    #     description={'placeholder': u'뒤는 무조건 @hufs.ac.kr!'}
    # )
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
        [validators.data_required(u'닉네임을 입력해주세요.(최대 7자)'),validators.length(max=7, message=u"최대 7자이내로 정해주세요.")],
        description={'placeholder': u'원하시는 닉네임!(최대 7자)'}
    )
    college = SelectField(
        u'소속대학', coerce=str, choices=[("상경대",u'상경대'),("사회과학대",u'사회과학대'),("경영대",u'경영대'),("영어대",u'영어대'),("서양어대",u'서양어대'),("동양어대",u'동양어대')
        ,("중국어대",u'중국어대'),("일본어대",u'일본어대'),("법대",u'법대'),("사범대",u'사범대'),("국제학부",u'국제학부'),("LD학부",u'LD학부'),("LT학부",u'LT학부')]
    )
    sex = SelectField(
        u'성별', coerce=int, choices=[(0,u'남자'),(1,u'여자')]
    )


class LoginForm(Form):
    code = StringField(
        u'외대 학번',
        [validators.data_required(u'외대 학번을 입력해주세요.')],
        description={'placeholder': u'외대 학번 입력하기!'}
    )
    password = PasswordField(
        u'비밀번호',
        [validators.data_required(u'비밀번호를 입력해주세요.')],
        description={'placeholder': u'비밀번호!'}
    )


class passwdResetEmailForm(Form):
    email = EmailField(
        u'이메일',
        [validators.data_required(u'이메일을 입력해주세요.')],
        description={'placeholder': u'인증받을 이메일을 입력해주세요'}
    )

class passwdResetConfirm(Form):
   password = PasswordField(
        u'비밀번호',
        [validators.data_required(u'새로운 비밀번호를 입력해주세요.'),
         validators.EqualTo('confirm_password', message=u'비밀번호가 일치하지 않습니다!')],
        description={'placeholder': u'새로운 비밀번호!'}
    )
   confirm_password = PasswordField(
        u'비밀번호 확인',
        [validators.data_required(u'비밀번를 한번 더 입력하세요.')],
        description={'placeholder': u'비밀번호 한번 더!'}
    )
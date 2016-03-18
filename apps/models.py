# -*- coding:utf-8 -*-
from apps import db
import pytz
import datetime

def get_current_time():
    return datetime.datetime.now(pytz.timezone('Asia/Seoul'))


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    code = db.Column(db.Integer)
    email = db.Column(db.String(255),default=0)
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255),index=True)
    #0은 남자 1은 여자
    sex = db.Column(db.Integer, default = 0)
    joinDATE = db.Column(db.DateTime(),default = get_current_time)
    college = db.Column(db.String(255))
    count = db.Column(db.Integer,default=0)
    level = db.Column(db.Integer, default = 0)

class Lecture(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), index=True)
    professor = db.Column(db.String(255), index=True)
    category = db.Column(db.String(255),index=True)
    year = db.Column(db.Integer, default = 0, index=True)
    semester = db.Column(db.Integer, default =0, index=True)
    get_grade = db.Column(db.Integer, default = 0)

    count = db.Column(db.Float, default = 0)
    total = db.Column(db.Float, default =0)
    difficulty = db.Column(db.Float, default =0)
    study_time = db.Column(db.Float, default =0)
    attendance = db.Column(db.Float, default =0)
    grade = db.Column(db.Float, default =0)
    achievement = db.Column(db.Float, default =0)

    def ev1(self):
        ev1=""
        if self.count == 0:
            ev1=0
        else:
            ev1 = self.total/self.count
        return ev1

    def ev2(self):
        ev2=""
        if self.count == 0:
            ev2=0
        else:
            ev2 = (self.difficulty/self.count) /5  * 100
        return ev2

    def ev3(self):
        ev3=""
        if self.count == 0:
            ev3=0
        else:
            ev3 = self.study_time/self.count /5  * 100
        return ev3
    def ev4(self):
        ev4=""
        if self.count == 0:
            ev4=0
        else:
            ev4 = self.attendance/self.count/5  * 100
        return ev4
    def ev5(self):
        ev5=""
        if self.count == 0:
            ev5=0
        else:
            ev5 = self.grade/self.count/5  * 100
        return ev5
    def ev6(self):
        ev6=""
        if self.count == 0:
            ev6=0
        else:
            ev6 = self.achievement/self.count /5  * 100
        return ev6


class Rating(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lecture = db.relationship('Lecture', backref=db.backref('rating_lecture', cascade='all, delete-orphan', lazy='dynamic'))
    lecture_id = db.Column(db.Integer, db.ForeignKey(Lecture.id))
    user = db.relationship('User', backref=db.backref('rating_user', cascade='all, delete-orphan', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    total = db.Column(db.Integer, default =0)
    difficulty = db.Column(db.Integer, default =0)
    study_time = db.Column(db.Integer, default =0)
    attendance = db.Column(db.Integer, default =0)
    grade = db.Column(db.Integer, default =0)
    achievement = db.Column(db.Integer, default =0)
    opinion = db.Column(db.Text())
    joinDATE = db.Column(db.DateTime(),default = get_current_time)

    def ev2(self):
        ev2 = self.difficulty /5  * 100
        return ev2

    def ev3(self):
        ev3 = self.study_time /5  * 100
        return ev3

    def ev4(self):
        ev4 = self.attendance /5  * 100
        return ev4

    def ev5(self):
        ev5 = self.grade /5  * 100
        return ev5

    def ev6(self):
        ev6 = self.achievement /5  * 100
        return ev6

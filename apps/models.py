# -*- coding:utf-8 -*-
from apps import db
import json
import urllib
import pytz
import datetime

def get_current_time():
    return datetime.datetime.now(pytz.timezone('Asia/Seoul'))


class User(db.Model):
    email = db.Column(db.String(255),primary_key=True)
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255),index=True)
    #0은 남자 1은 여자
    sex = db.Column(db.Integer, default = 0)
    joinDATE = db.Column(db.DateTime(),default = db.func.now())
    prefsVideo = db.Column(db.Text(length=None, collation=None, convert_unicode=False, unicode_error=None, _warn_on_bytestring=False))
    prefsActor = db.Column(db.Text(length=None, collation=None, convert_unicode=False, unicode_error=None, _warn_on_bytestring=False))
    numVideo = db.Column(db.Integer, default=0, index=True)
    numActor = db.Column(db.Integer, default=0, index=True)
    # 각 유저마다 {'영상':평점 ... } 형태로 dict 리턴
    def ratings(self):
        dict = {}
        for oRating in self.ratingVideo_user:
            dict[oRating.videoName] = oRating.rating
        return dict
    def ratingsActor(self):
        list = []
        for oRating in self.ratingActor_user:
            list.append(dict(name=oRating.actorName,rating=oRating.rating))
        return list
    def ratingsVideo(self):
        list = []
        for oRating in self.ratingVideo_user:
            list.append(dict(name=oRating.videoName,rating=oRating.rating))
        return list
    def aRatings(self):
        dict = {}
        for oRating in self.ratingActor_user:
            dict[oRating.actorName] = oRating.rating
        return dict

class Actor(db.Model):
    name = db.Column(db.String(255),primary_key=True)
    height =db.Column(db.Integer, default=0)
    score = db.Column(db.Float, default =0)
    count = db.Column(db.Integer, default = 0 ,index=True)
    average = db.Column(db.Float, default=0)
    age = db.Column(db.Integer, default = 0)
    release = db.Column(db.Float, default=0, index=True)
    category = db.Column(db.String(255),index=True)
    prefs = db.Column(db.Text(length=None, collation=None, convert_unicode=False, unicode_error=None, _warn_on_bytestring=False))
    # 모델 차원에서 리스트를 생성하는 함수를 생성
    # each.reviews() 실행하면 댓글 각 한 줄을 dict로 갖는 리스트를 리턴함
    # 댓글 각 한줄 및 전체 리스트는 javascript가 인식 가능하게 json형태로 리턴!
    def ratedPerson(self):
        dict = {}
        for oRating in self.ratingActor_actor:
            dict[oRating.userEmail] = oRating.rating
        return dict
    def url(self):

        # url = u'http://storage.googleapis.com/jikbakguri/actor2/'+str(self.name)+'.jpg'
        # a = urllib.quote(url.encode('utf8'), '/:')
        # return a
        return 'http://storage.googleapis.com/jikbakguri/actor2/'+self.name+'.jpg'

    def yesfile(self):
        a = urllib.quote(str(self.name).encode('euc-kr'))
        url = u'http://www.yesfile.com/partner/link.php?pid=jikbakguri&div=AD&ss=all&sc='+a

        return url

    def reviews(self):
        list = [] # return할 list
        for review in self.actorReview_actor:
            numVideo = review.user.numVideo
            if numVideo<50:
                sLevel= 0
            elif 50<=numVideo<100:
                sLevel= 1
            elif 100<=numVideo<200:
                sLevel= 2
            elif 200<=numVideo<400:
                sLevel= 3
            else:
                sLevel= 4
            list.append( dict(id = review.id, author=review.user.nickname, content=review.content,level=sLevel))
        return list

    def videos(self):
        list=[]
        for each in self.filmo_actor:
            list.append(dict(name = each.video.name, average = each.video.average))
        return list



class Video(db.Model):
    name = db.Column(db.String(255),primary_key=True)
    category = db.Column(db.String(255),index=True)
    #노모가 0, 유모가 1
    exposure = db.Column(db.Integer, default=1)
    release = db.Column(db.Float, default=0, index=True)
    score = db.Column(db.Float, default =0)
    count = db.Column(db.Integer, default = 0, index=True)
    average = db.Column(db.Float, default=0)
    company =db.Column(db.String(255), index=True)
    prefs = db.Column(db.Text(length=None, collation=None, convert_unicode=False, unicode_error=None, _warn_on_bytestring=False))
    def ratedPerson(self):
        dict = {}
        for oRating in self.ratingVideo_video:
            dict[oRating.userEmail] = oRating.rating
        return dict
    def url(self):
        return 'http://storage.googleapis.com/jikbakguri/video/'+self.name+'.jpg'
    def reviews(self):
        list = [] # return할 list
        for review in self.videoReview_video:
            numVideo = review.user.numVideo
            if numVideo<50:
                sLevel= 0
            elif 50<=numVideo<100:
                sLevel= 1
            elif 100<=numVideo<200:
                sLevel= 2
            elif 200<=numVideo<400:
                sLevel= 3
            else:
                sLevel= 4
            list.append( dict(id = review.id, author=review.user.nickname, content=review.content,level=sLevel))
        return list

    def actors(self):
        list= []

        for each in self.filmo_video:
            list.append(dict(name = each.actor.name, average = each.actor.average))
        return list

class ActorReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('actorReview_actor', cascade='all, delete-orphan', lazy='dynamic'))
    actorName = db.Column(db.String(255), db.ForeignKey(Actor.name))
    user = db.relationship('User', backref=db.backref('actorReview_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    content = db.Column(db.String(68))
    created=db.Column(db.Date(), default=db.func.now())

class VideoReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('videoReview_video', cascade='all, delete-orphan', lazy='dynamic'))
    videoName = db.Column(db.String(255), db.ForeignKey(Video.name))
    user = db.relationship('User', backref=db.backref('videoReview_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    content = db.Column(db.String(68))
    created=db.Column(db.Date(), default=db.func.now())

class Filmo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('filmo_actor', cascade='all, delete-orphan', lazy='dynamic'))
    video = db.relationship('Video', backref=db.backref('filmo_video', cascade='all, delete-orphan', lazy='dynamic'))
    videoName = db.Column(db.String(255), db.ForeignKey(Video.name))
    ActorName = db.Column(db.String(255), db.ForeignKey(Actor.name))


class RatingActor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('ratingActor_actor', cascade='all, delete-orphan', lazy='dynamic'))
    actorName = db.Column(db.String(255), db.ForeignKey(Actor.name))
    user = db.relationship('User', backref=db.backref('ratingActor_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    rating = db.Column(db.Integer, default=0)

class RatingVideo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('ratingVideo_video', cascade='all, delete-orphan', lazy='dynamic'))
    videoName = db.Column(db.String(255), db.ForeignKey(Video.name))
    user = db.relationship('User', backref=db.backref('ratingVideo_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    rating = db.Column(db.Integer, default=0)

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.relationship('User', backref=db.backref('favorite_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    actor = db.relationship('Actor', backref=db.backref('favorite_actor', cascade='all, delete-orphan', lazy='dynamic'))
    actorName = db.Column(db.String(255), db.ForeignKey(Actor.name))

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video = db.relationship('Video', backref=db.backref('bookmark_video',cascade='all, delete-orphan',lazy='dynamic'))
    videoName=db.Column(db.String(255), db.ForeignKey(Video.name))
    user = db.relationship('User', backref=db.backref('bookmark_user',cascade='all, delete-orphan',lazy='dynamic'))
    userEmail=db.Column(db.String(255), db.ForeignKey(User.email))



# class Notice(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nickname = db.Column(db.String(255))
#     title = db.Column(db.String(255))
#     content = db.Column(db.Text())
#     category = db.Column(db.Integer,default=0)
#     click = db.Column(db.Integer,default =0)
#     commentCount = db.Column(db.Integer, default=0)
#     created = db.Column(db.DateTime(), default=db.func.now())
#
#
# class Review(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     notice = db.relationship('BoardNotice', backref=db.backref('noticeReview_notice', cascade='all, delete-orphan', lazy='dynamic'))
#     noticeId = db.Column(db.Integer, db.ForeignKey(BoardNotice.id))
#     user = db.relationship('User', backref=db.backref('noticeReview_user', cascade='all, delete-orphan', lazy='dynamic'))
#     userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
#     content = db.Column(db.Text())
#     created = db.Column(db.DateTime(), default=db.func.now())


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    user = db.relationship('User',backref=db.backref('board_user', cascade='all, delete-orphan', lazy='dynamic'))
    nickname = db.Column(db.String(255))
    title = db.Column(db.String(120))
    content = db.Column(db.Text())
    category = db.Column(db.Integer,default=0)
    like = db.Column(db.Integer,default = 0)
    hate = db.Column(db.Integer,default = 0)
    click = db.Column(db.Integer,default =0)
    commentCount = db.Column(db.Integer,default =0)
    created = db.Column(db.DateTime(), default=get_current_time)


class BoardReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    board = db.relationship('Board', backref=db.backref('boardReview_board', cascade='all, delete-orphan', lazy='dynamic'))
    boardId = db.Column(db.Integer, db.ForeignKey(Board.id))
    user = db.relationship('User', backref=db.backref('boardReview_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    content = db.Column(db.Text())
    created = db.Column(db.DateTime(), default=get_current_time)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    user = db.relationship('User', backref=db.backref('like_user', cascade='all, delete-orphan', lazy='dynamic'))
    boardId = db.Column(db.Integer, db.ForeignKey(Board.id))
    board = db.relationship('Board', backref = db.backref('like_board', cascade='all, delete-orphan', lazy='dynamic'))
    #like 0 , hate 1
    evaluate = db.Column(db.Integer,default=0)


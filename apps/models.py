# -*- coding:utf-8 -*-
from apps import db

class User(db.Model):
    email = db.Column(db.String(255),primary_key=True)
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    joinDATE = db.Column(db.DateTime(),default = db.func.now())

class Actor(db.Model):
    name = db.Column(db.String(255),primary_key=True)
    image = db.Column(db.LargeBinary)
    category =db.Column(db.String(255))
    score = db.Column(db.Float, default =0)
    count = db.Column(db.Integer, default = 0)
    average = db.Column(db.Float, default=0)

class Video(db.Model):
    name = db.Column(db.String(255),primary_key=True)
    image = db.Column(db.LargeBinary)
    category = db.Column(db.String(255))
    #노모가 0, 유모가 1
    exposure = db.Column(db.Integer, default=1)
    release = db.Column(db.Integer, default=0)
    score = db.Column(db.Float, default =0)
    count = db.Column(db.Integer, default = 0)
    average = db.Column(db.Float, default=0)

class ActorReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('actorReview_actor', cascade='all, delete-orphan', lazy='dynamic'))
    actorName = db.Column(db.String(255), db.ForeignKey(Actor.name))
    user = db.relationship('User', backref=db.backref('actorReview_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    content = db.Column(db.Text())
    created=db.Column(db.Date(), default=db.func.now())

class VideoReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('videoReview_video', cascade='all, delete-orphan', lazy='dynamic'))
    videoName = db.Column(db.String(255), db.ForeignKey(Video.name))
    user = db.relationship('User', backref=db.backref('videoReview_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    content = db.Column(db.Text())
    created=db.Column(db.Date(), default=db.func.now())

class Filmo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('filmo_actor', cascade='all, delete-orphan', lazy='dynamic'))
    video = db.relationship('Video', backref=db.backref('filmo_video', cascade='all, delete-orphan', lazy='dynamic'))
    videoName = db.Column(db.String(255), db.ForeignKey(Video.name))
    ActorName = db.Column(db.String(255), db.ForeignKey(Actor.name))

class RatingActor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('rating_actor', cascade='all, delete-orphan', lazy='dynamic'))
    actorName = db.Column(db.String(255), db.ForeignKey(Video.name))
    user = db.relationship('User', backref=db.backref('rating_user', cascade='all, delete-orphan', lazy='dynamic'))
    userEmail = db.Column(db.String(255), db.ForeignKey(User.email))
    rating = db.Column(db.Integer, default=0)

class RatingVideo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('rating_video', cascade='all, delete-orphan', lazy='dynamic'))
    videoName = db.Column(db.String(255), db.ForeignKey(Video.name))
    user = db.relationship('User', backref=db.backref('rating_user', cascade='all, delete-orphan', lazy='dynamic'))
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



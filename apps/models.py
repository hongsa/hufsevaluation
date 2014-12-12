# -*- coding:utf-8 -*-
from apps import db


# actor_video = db.Table('actor_video',
#     db.Column('actor_name', db.String(255), db.ForeignKey('actor.name')),
#     db.Column('video_name', db.String(255), db.ForeignKey('video.name'))
# )


class User(db.Model):
    email = db.Column(db.String(255), primary_key = True)
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    join_date = db.Column(db.DateTime(),default = db.func.now())


class Actor(db.Model):
    name = db.Column(db.String(255), primary_key = True)
    image = db.Column(db.LargeBinary)
    age = db.Column(db.Integer, default=0)
    body_size = db.Column(db.String(255), default =0)
    active_year = db.Column(db.Integer, default=0)
    similar_actor = db.Column(db.String(255))
    category =db.Column(db.String(255))
    score = db.Column(db.Integer, default =1)
    count = db.Column(db.Integer, default = 1)
    # actor_video = db.relationship('actor_video', secondary=actor_video, backref=db.backref('actors', lazy='dynamic'))


class Actor_review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('actor_reviews', cascade='all, delete-orphan', lazy='dynamic'))
    actor_name = db.Column(db.String(255), db.ForeignKey(Actor.name))
    user = db.relationship('User', backref=db.backref('user_actor_reviews', cascade='all, delete-orphan', lazy='dynamic'))
    user_email = db.Column(db.String(255), db.ForeignKey(User.email))
    content = db.Column(db.Text())
    date_created=db.Column(db.DateTime(), default=db.func.now())

class Video(db.Model):
    name = db.Column(db.String(255), primary_key=True)
    image = db.Column(db.LargeBinary)
    category = db.Column(db.String(255))
    release_year = db.Column(db.Integer, default=0)
    exposure = db.Column(db.String(255))
    score_total = db.Column(db.Integer, default=1)
    score_count = db.Column(db.Integer, default=1)

    # def image_url(self):
    #     # return '/show2/ff1234'
    #     return url_for('show2', key=self.name)

    # video_actor = db.relationship('actor_video', secondary=actor_video, backref=db.backref('videos', lazy='dynamic'))
    # review=db.Column(db.Text())

class Video_review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('video_reviews', cascade='all, delete-orphan', lazy='dynamic'))
    video_name = db.Column(db.String(255), db.ForeignKey(Video.name))
    # test=Video_review()
    # test.User.nickname
    user = db.relationship('User', backref=db.backref('user_grade', cascade='all, delete-orphan', lazy='dynamic'))
    # author=db.relationship('User', backref=db.backref('user_grade', cascade='all, delete-orphan', lazy='dynamic'))
    user_email = db.Column(db.String(255), db.ForeignKey(User.email))
    # grade = db.Column(db.Integer, default=0)
    content = db.Column(db.Text())
    date_created=db.Column(db.DateTime(), default=db.func.now())

class Actor_Video(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor_video = db.relationship('Actor', backref=db.backref('actor_video', cascade='all, delete-orphan', lazy='dynamic'))
    video_actor = db.relationship('Video', backref=db.backref('video_actor', cascade='all, delete-orphan', lazy='dynamic'))
    actor_name = db.Column(db.String(255), db.ForeignKey(Actor.name))
    video_name = db.Column(db.String(255), db.ForeignKey(Video.name))

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('video_rating', cascade='all, delete-orphan', lazy='dynamic'))
    video_rating = db.Column(db.String(255), db.ForeignKey(Video.name))
    user = db.relationship('User', backref=db.backref('user_rating', cascade='all, delete-orphan', lazy='dynamic'))
    user_rating = db.Column(db.String(255), db.ForeignKey(User.email))
    rating = db.Column(db.Integer, default=0)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.relationship('User', backref=db.backref('user_bookmark', cascade='all, delete-orphan', lazy='dynamic'))
    user_email = db.Column(db.String(255), db.ForeignKey(User.email))
    actor = db.relationship('Actor', backref=db.backref('actor_bookmark', cascade='all, delete-orphan', lazy='dynamic'))
    actor_name = db.Column(db.String(255), db.ForeignKey(Actor.name))



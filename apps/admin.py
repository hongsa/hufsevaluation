# -*- coding:utf-8 -*-
from flask import redirect,url_for,request,g
from apps import db,app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import User,Lecture

class UserModelView(ModelView):
    def is_accessible(self):
        if g.user is None:
            return False
        else:
            if g.user.level == 1:
                return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index', next=request.url))

    can_delete = False
    can_create = False
    can_edit = False
    column_exclude_list = ['password','email']
    column_searchable_list = ['code',]
    column_editable_list = ['nickname']
    column_filters = ['college', 'count', 'joinDATE']
    form_excluded_columns = ['code']

class LectureModelView(ModelView):
    def is_accessible(self):
        if g.user is None:
            return False
        else:
            if g.user.level == 1:
                return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index', next=request.url))

    can_delete = False
    can_create = False
    can_edit = False
    column_exclude_list = ['count','total','difficulty','study_time','attendance','grade','achievement']
    column_editable_list = ['name','professor','category','semester','get_grade','year']
    column_searchable_list = ['name','professor']
    column_filters = ['category']

class RatingModelView(ModelView):
    can_delete = False
    can_create = False


admin = Admin(app, name='static', template_mode='bootstrap3', url='/static')
admin.add_view(UserModelView(User, db.session))
admin.add_view(LectureModelView(Lecture, db.session))
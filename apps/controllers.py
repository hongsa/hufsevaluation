# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response,current_app
from apps import app,db
<<<<<<< HEAD
=======
from apps.core.model.models import Actor, Filmo, Rating, Bookmark
from core.model import models as models
from core.controller import userController as userC
from core.controller import videoController as videoC
from core.controller import actorController as actorC
from core.service import ratings as ratings
from core.service import image as image
from core.service import admin as adminS
from core.service import etc as etc
>>>>>>> 942b695f89142e7c04f229f050afee774b83fe82


@app.route('/')

@app.route('/index')
def index():
    return render_template("main_page.html")

@app.route('/category')
def category_main():
	return render_template("category_layout.html")





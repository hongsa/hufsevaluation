# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, make_response,current_app
from apps import app,db

@app.route('/')

@app.route('/index')
def index():
    return render_template("main_page.html")

@app.route('/category')
def category_main():
	return render_template("category_layout.html")

@app.route('/video_main')
def video_main():
	return render_template("video_main.html")

@app.route('/actress_main')
def actress_main():
	return render_template("actress_main.html")

@app.route('/new_video_main')
def new_video_main():
	return render_template("new_video_main.html")

@app.route('/crawl')
def crawl():
    if request.method == 'GET':
        basicurl = "https://www.google.co.kr/search?q="
        url = basicurl + request.args['search'] + ' ' + 'torrent'
        return redirect(url)

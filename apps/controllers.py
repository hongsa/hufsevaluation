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





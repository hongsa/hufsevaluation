from flask import redirect, url_for, render_template,flash, session, current_app
from sqlalchemy import desc
from apps.models import User,Lecture
import random
from  sqlalchemy.sql.expression import func
import time,logging,json

def main_page():
    if not 'session_user_email' in session:
        return redirect(url_for('index'))

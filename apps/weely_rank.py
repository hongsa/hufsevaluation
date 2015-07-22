import logging
from sqlalchemy import desc
from flask import redirect, url_for, render_template,flash, session, current_app
from sqlalchemy import desc,asc
from apps.models import Actor,User,ActorReview,RatingActor,Video,VideoReview,RatingVideo
import random
from  sqlalchemy.sql.expression import func
import time,logging,json
import pytz
import datetime
import logging


def get_current_time():
    return datetime.datetime.now(pytz.timezone('Asia/Seoul'))

def get_1week_ago():
    return get_current_time() - datetime.timedelta(weeks=1)

def weekly():

    from sqlalchemy import func
    from  sqlalchemy.sql.expression import func
    from sqlalchemy.sql import func
    from apps import db
    from apps.models import RatingVideo,RatingActor,Actor

    rating_actor = RatingActor.query.filter(RatingActor.created >= get_1week_ago()).add_columns(func.sum(RatingActor.rating)).group_by(RatingActor.actorName).order_by(db.func.sum(RatingActor.rating).desc()).limit(10)


    for each in rating_actor:
        logging.error(each[0].actorName)
        logging.error(each[1])



    return "end"

weekly()



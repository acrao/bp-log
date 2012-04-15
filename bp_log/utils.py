from bp_log import app

import flask
from functools import wraps
from google.appengine.api import users

def login_required(func):

    @wraps(func)
    def check_logged_in(*args, **kwargs):
        user = users.get_current_user()
        if not user:
            return flask.redirect(users.create_login_url(dest_url=flask.request.url))
        return func(*args, **kwargs)
    return check_logged_in

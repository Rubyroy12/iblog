from . import main
from flask import render_template,redirect, url_for,abort
from flask_login import login_required, current_user

from .. import db

@main.route('/')
def index():

    return render_template('index.html' , current_user=current_user)

from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app, send_from_directory, session, jsonify
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user


import base64
import imghdr
import random
from datetime import datetime, timedelta
import datetime as dt

from . import DateToolKit as dtk
from .db import db
from .db import dbORM
from . import encrypt
from . import ScreenGoRoute
from . import function_pool
from . import id_generator

views = Blueprint('views', __name__)

@views.route("/")
def renderLandingPage():

    return render_template("Landing.html")

@views.route("/home")
@login_required
def renderHome():

    return ScreenGoRoute.route("1")
from flask import Flask, render_template, request, flash, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, logout_user, current_user, login_user, UserMixin

import json
import os
import random

from .db import db
from .db import dbORM
from .encrypt import encrypter
from .DateToolKit import split_date
from . import id_generator
from . import function_pool

from . import ScreenGoRoute


def initialize_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdadsadakmi23e'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__).replace('\\', '/'), 'static/_UM_')
    print(f"UF: ({UPLOAD_FOLDER})")

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from .user_actions import user_actions
    from .views import views

    app.register_blueprint(user_actions, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    @app.errorhandler(500)
    def internal_server_error(e, err_code=500):
        app.logger.error(f"Internal Server Error: {e}")
        return render_template('broken-page.html', error=e, code=err_code), 500

    @app.errorhandler(404)
    def internal_server_error(e, err_code=404):
        app.logger.error(f"Route Not Found: {e}")
        return render_template('broken-page.html', error=e, code=err_code), 404

    # @app.errorhandler(500)
    # def internal_server_error(e, err_code=500):
    #     app.logger.error(f"Internal Server Error: {e}")
    #     return render_template('broken-page.html', error=e, code=err_code), 500

    from flask_login import UserMixin, LoginManager

    FL_Login = LoginManager(app)
    FL_Login.login_view = 'login'

    class UserClass:
        def __init__(self, id):
            self.id = id

        @staticmethod
        def is_authenticated():
            return True

        @staticmethod
        def is_active():
            return True

        @staticmethod
        def is_anonymous():
            return False

        def get_id(self):
            return self.id


        @FL_Login.user_loader
        def load_user(id):
            try:
                u = dbORM.find_one("UserSICT", "id", id)
                if not u:
                    return None
                return UserClass(id=dbORM.get_all("UserSICT")[f'{u}']['id'])
            except:#Skipp
                anonymous = {
                    "0": {
                        "id": "0", 
                        "email": "NULL"
                    }
                }
                return UserClass(id=anonymous['0']['id'])


    @app.route("/login", methods=['GET', 'POST']) 
    def login():
        User = dbORM.get_all("UserSICT")

        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = dbORM.find_one("UserSICT", "email", email)

            if user and check_password_hash(dbORM.get_all("UserSICT")[f'{user}']['password'], password):
                t_user = UserClass(id=f'{user}')
                login_user(t_user, remember=True)
                return redirect(url_for('user_actions.viewDashboard'))
                
            else:
                return render_template("login.html", DeviceType=function_pool.detectDeviceType(request), status=("Incorrect password or email.", "Error occurred"))

        return render_template('login.html', DeviceType=function_pool.detectDeviceType(request), status=("", "None"))

    @app.route("/signup", methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            country = request.form.get("Country")

            phone_number = request.form.get('phone_number')
            email = request.form.get('email')
            email_address = email

            password = request.form.get("password")

            user = dbORM.find_one("UserSICT", 'email', email)

            if user:
                return render_template("signup.html", DeviceType=function_pool.detectDeviceType(request), status=("Email is already taken.", "Sign Up Error", "2"))
            elif len(email) < 4:
                return render_template("signup.html", DeviceType=function_pool.detectDeviceType(request), status=("Email must be at least 4 characters long.", "Sign Up Error", "3"))

            elif len(first_name) < 2 or len(last_name) < 2:
                return render_template("signup.html", DeviceType=function_pool.detectDeviceType(request), status=("Name must be at least 2 characters long.", "Sign Up Error", "1"))
            
            elif password != password:
                return render_template("signup.html", DeviceType=function_pool.detectDeviceType(request), status=("Passwords do not match. Please re-enter your password.", "Sign Up Error", "1"))

            elif len(password) < 8:
                return render_template("signup.html", DeviceType=function_pool.detectDeviceType(request), status=("Password is too short. It must be at least 8 characters long.", "Sign Up Error", "1"))
            else:
                numbers = []
                for x in range(10):
                    numbers.append(x)
                new_user = {
                    "first_name": first_name,
                    "last_name": last_name, 
                    "email": "", 
                    "password": "", 
                    "phone_number": "", 
                    "user_type": "", 
                    "gender": "", 
                    "department": "", 
                    "school_level": "",
                    "school_year": "", 
                    "address": "", 
                    "nin": "", 
                    "dob": ""
                }

                # for key, details in new_user.items():
                dbORM.add_entry("UserSICT", f"{encrypter(str(new_user))}")

                t_user = UserClass(id=f'{dbORM.find_one("UserSICT", "email", email)}')

                login_user(t_user, remember=True)

                return redirect(url_for('user_actions.viewDashboard'))

        return render_template("signup.html", DeviceType=function_pool.detectDeviceType(request), status=("", "None", "1"), ref_codee="NULL")
        

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash("Logged out successfully.", category='Success') 
        return redirect(url_for('login'))
    

    return app
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from .db import dbORM
from . import DateToolKit as dtk

import base64
import imghdr
from . import encrypt
import random
from . import function_pool
import datetime as dt
from datetime import datetime

User, Record = dbORM.get_all("UserSICT"), None
	

def go_to(screen_id, _redirect=False, **kwargs):
	if _redirect == False:
		u = dbORM.get_all("UserSICT")[f'{current_user.id}']
		
		if screen_id != "1":
			return render_template(f"{screen_id}",
				CUser = u,		

				ScreenID = screen_id,

				DTK = dtk,
				LengthFunc = len,
				ToJoin = function_pool.toJoin,
				DeviceType = function_pool.detectDeviceType(kwargs['request']),
				GetDBItem = function_pool.getDBItem,
				ToString = str,
				PythonEval = eval,
				ToFloat = float,
				ToFloatToInt = function_pool.floatToInt,
				Thousandify = function_pool.thousandify,
				StandardCurrency = "NGN",
				getMIME = function_pool.get_mime_type,
				TimeDifference = function_pool.calcTimeDifference,
				CurrentTime = function_pool.getDateTime()[1],
				HTMLBreak_ = function_pool.HTMLBreak
			)
		else:
			return render_template("Profile.html",
				CUser = u,		

				ScreenID = screen_id,

				DTK = dtk,
				LengthFunc = len,
				ToJoin = function_pool.toJoin,
				DeviceType = function_pool.detectDeviceType(kwargs['request']),
				GetDBItem = function_pool.getDBItem,
				ToString = str,
				PythonEval = eval,
				ToFloat = float,
				ToFloatToInt = function_pool.floatToInt,
				Thousandify = function_pool.thousandify,
				StandardCurrency = "NGN",
				getMIME = function_pool.get_mime_type,
				TimeDifference = function_pool.calcTimeDifference,
				CurrentTime = function_pool.getDateTime()[1],
				HTMLBreak_ = function_pool.HTMLBreak
			)
	else:
		return redirect(url_for("views.dashboard"))
	
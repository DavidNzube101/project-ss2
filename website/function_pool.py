from .db import dbORM
import base64
import imghdr
import datetime as dt
from datetime import datetime, timedelta
from flask_login import login_required, current_user
from . import DateToolKit as dtk
import math as Math
from . import id_generator
from . import encrypt



def calcTimeDifference(dpt, ct):
	return [int(x) for x in ("[" + str(datetime.strptime(dpt, "%H:%M") - datetime.strptime(ct, "%H:%M:%S")).replace(":", ", ").replace("-1 day, ", "") + "]").strip("[]").split(", ")]

def getDBItem(model, column, value):
	
	try:
		i = dbORM.get_all(model)[f'{dbORM.find_one(model, column, value)}']
	except Exception as e:
		i = {}

	return i

def loopAppendAndReverse(a, b):
	try:
		for k, v in a.items():
			b.append(v)
		return b[::-1]
	except Exception as e:
		return f"Error occured\nError: {e}"

def toJoin(i, j):
	return f"{i}{j}"

def thousandify(amount):
	amount = "{:,}".format(float(amount))
	return f"{amount}"

def is_test():
	return "True"

def floatToInt(n):
	return f"{Math.ceil(float(n))}"

def StandardCurrency():
	return "NGN"

def getDateTime():
	# Getting Date-Time Info
	current_date = dt.date.today()
	current_time = datetime.now().strftime("%H:%M:%S")

	# Date Format: "YYYY-MM-DD"
	formatted_date = current_date.strftime("%Y-%m-%d")
	date = formatted_date
	time = current_time

	return [date, time]

def HTMLBreak(n):
	breaks = ""

	for x in range(int(n)):
		breaks = breaks + "\n<br>"	

	return breaks

def getOppositeTheme(theme):
	if theme == 'light':
		return 'dark'
	else:
		return 'light'

def oppositeCurrency(currency):
	return "NGN" if currency == "$" else "NGN"


def detectDeviceType(theRequest):
	user_agent = theRequest.user_agent.string.lower()

	if 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
	  device_type = 'Mobile'
	else:
	  device_type = 'Desktop'

	return device_type


def get_mime_type(data):
    decoded_data = base64.b64decode(data)
    image_type = imghdr.what(None, h=decoded_data)
    return f'image/{image_type}' if image_type else 'application/pdf'
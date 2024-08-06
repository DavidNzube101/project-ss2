import requests
from . import encrypt
from . import __trash

# CON_KEY = "david.nzube.official22@gmail.com/david.nzube.official22@gmail.com/8x7bty112(8jIj8*22@P21=+~-+1.m"
CON_KEY = encrypt.decrypter(encrypt.decrypter(encrypt.decrypter(encrypt.decrypter((__trash.retTr())))))

from_ = "http://127.0.0.1:781"
# from_ = "https://sarahdb.pythonanywhere.com"

link_prefix = f"{from_}/{CON_KEY}/handler"

DB_URL = f"{from_}/login/{CON_KEY}"


try:
	response = requests.get(DB_URL)

	def connect():
		requests.get(DB_URL)

	def request_then_text(url):
		req = requests.get(url)
		return req.text

	def request_then_text_post(url, data):
		req = requests.post(url, data)
		return req.text

	if (response.status_code):
		print("connected to db server successfully")
		print(f"\n\n>>>>>>>>>>>>>>>>>>>>>{response.text}\n\n\n")

		db = {}

		class dbORM:
			"""docstring for dbORM"""
			def __init__(self):
				self.database = db

			def all():
				# connect()
				return eval(request_then_text(url=f'{link_prefix}/handler'))

			def get_all(model):
				# connect()
				return eval(request_then_text(url=f'{link_prefix}/get_all/{model}'))

			def find_all(model, column, value):
				return eval(request_then_text(url=f'{link_prefix}/find_all/{model}/{column}/{value}'))

			def add_one(model, column, value):
				# connect()
				return eval(request_then_text(url=f'{link_prefix}/add_one/{model}/{column}/{value}'))

			def add_entry(model, column_value_pairs):
				try:
					return eval(request_then_text(url=f'{link_prefix}/add_entry/{model}/{column_value_pairs}'))
				except Exception as e:
					print(f">>>>>>>>>>>>>>>>>>>>>>>>>>\ne: {e}\nmodel: {model}\ncvp: {column_value_pairs}")

			def find_one(model, column, value):
				return eval(request_then_text(url=f'{link_prefix}/find_one/{model}/{column}/{value}'))

			def update_one(model, column, value_search, value_update):
				# connect()
				return eval(request_then_text(url=f'{link_prefix}/update_one/{model}/{column}/{value_search}/{value_update}'))

			def update_entry(model, column, column_value_pairs, dnd):
				if dnd == True:
					_ = {
						"model": f"{model}", 
						"column": f"{column}", 
						"cvp": f"{column_value_pairs}"
					}
					return eval(request_then_text_post(url=f'{link_prefix}/update_entry_dnd', data=_))
				else:
					return eval(request_then_text(url=f'{link_prefix}/update_entry/{model}/{column}/{column_value_pairs}'))
				

			def delete_entry(model, column):
				return eval(request_then_text(url=f'{link_prefix}/delete_entry/{model}/{column}'))
				

	else:
		print("error connecting to db server")
		dbORM = None
except Exception as e:
	print(f"\n\n\n\nerror>>>>>>>>>> {e}\n\n\n\n")
	db = None
	dbORM = None
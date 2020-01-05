#存储数据1004-1
'''
#number_writer.py
import json

numbers = [2,3,5,7,9]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)

#number_rader.py
import json

filename = 'numbers.json'
with open(filename) as f_obj:
	numbers =json.load(f_obj)
	
print(numbers)

import json

username = input("What's your name?")

filename = 'username.json'

with open(filename,'w') as f_obj: 
	json.dump(username,f_obj)
	print("We remember you when you come back, " + username + "！")

import json

filename = 'username.json'

with open(filename) as f_obj:
	username =json.load(f_obj)
	print("Welcom back," + username + "!")
'''
import json


def get_stored_username():
	#如果存储了用户名，就获取它
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username =json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
	
def greet_user():	
	#问候用户
	username = get_stored_username()
	if username:
		print("Welcom back," + username + "!")
	else:
		username = input("What's your name?")
		filename = "username.json"
		with open(filename,'w') as f_obj: 
			json.dump(username,f_obj)
			print("We remember you when you come back, " + username + "！")

greet_user()


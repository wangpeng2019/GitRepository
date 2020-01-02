'''
#greeter.py
def greet_user(username):
	#显示打印信息
	print("hello,"+username.title()+"!")
	
greet_user('wangpeng')
'''

#pets.py
def describe_pet(animal_type,pet_name):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('hamster','harry')
describe_pet('dog','willer')

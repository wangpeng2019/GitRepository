'''
#greeter.py
def greet_user(username):
	#显示打印信息
	print("hello,"+username.title()+"!")
	
greet_user('wangpeng')
'''

#pets.py
def describe_pet(pet_name,animal_type='dog'):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')

'''
#greeter.py
def greet_user(username):
	#显示打印信息
	print("hello,"+username.title()+"!")
	
greet_user('wangpeng')


#pets.py
def describe_pet(pet_name,animal_type='dog'):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')
'''
#formatted_name.py
#返回值
def get_formatted_name(first_name,last_name):
	'''返回整洁的姓名'''
	full_name=first_name + ' ' + last_name
	return full_name.title()

musician=get_formatted_name('jimi','hedrix')
print(musician)

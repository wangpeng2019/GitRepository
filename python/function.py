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


#formatted_name.py
#返回值
def get_formatted_name(first_name,last_name,middle_name=''):
	#返回整洁的姓名
	full_name=first_name + ' ' + last_name
	return full_name.title()
	
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	
	f_name=input("first name:")
	if f_name =='q':
		break
		
	l_name=input("last name:")
	if l_name=='q':
		break
		
	formated_name=get_formatted_name(f_name,l_name)
	print("\nHello,"+ formated_name+" !")


#返回字典
def build_person(first_name,last_name,age=''):
	#将person定义为字典
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
	
mus=build_person('jimi','hend',age= 27)
print(mus)


#传递列表
#greet_users.py
def greet_users(names):
	#向列表中每位用户发出简单问候
	for name in names:
		msg="Hello," + name.title() + "!"
		print(msg)
		
usernames=['lixiaoqin','hewangpeng','lover']
greet_users(usernames)
'''








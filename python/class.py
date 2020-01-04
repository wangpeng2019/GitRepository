#创建dog类
#dog.py
class Dog():
	#模拟小狗的简单尝试
	
	def __init__(self,name,age):
		#初始化属性name age
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		print(self.name.title() + " is rolled over!")

my_dog = Dog('while',6)
my_dog.sit()
my_dog.roll_over()

print("My dog's name is " + my_dog.name.title()+ ".")
print("my dog is " +str(my_dog.age) + " years old.")



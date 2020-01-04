'''
#01-创建dog类
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
'''

#02-创建car类
#car.py
class Car():
	#模拟汽车
	def __init__(self,make,model,year):
		#初始化描述汽车的属性
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
		
		
	def get_descriptive_name(self):
		#返回描述信息
		long_name=str(self.year) + self.make + self.model
		return long_name.title()
	
	def read_odometer(self):
		#将汽车里程信息打印出来
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):
		#更新里程表的值,并禁止回调里程表
		if mileage >= self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self,miles):
		#定量增加里程数
		self.odometer_reading +=miles

from car import Car
#给类定义属性

class Battery():
	#模拟电动汽车电瓶
	def __init__(self,battery_size=70):
		#初始化电瓶的属性
		self.battery_size=battery_size
	
	def describe_battery(self):
		#打印电瓶容量信息
		print("This car has a  " + str(self.battery_size) + "-kwh battery.")
		
	def get_range(self):
		#打印一条信息，指出电瓶的续航里程
		if self.battery_size == 70:
			range=240
		elif self.battery_size == 85:
			range=270
			
		message="This car can go " + str(range)
		message+= "mils on a full charge."
		print(message)
		
		
#03使用继承
class ElectriCar(Car):
	#电动汽车的特殊之处
	
	def __init__(self,make,model,year):
		#初始化父类的属性
		super().__init__(make,model,year)
		#初始化电动车特有属性
		self.battery = Battery()
		

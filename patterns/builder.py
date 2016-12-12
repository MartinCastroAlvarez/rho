""" Builder pattern applied to Python by martincastro.10.5@gmail.com """

class Car:

	def __init__(self):
		self.name  = str()
		self.color = str()
		self.price = float()

class CarBuilder: 

	def __init__(self,name,color,price):
		self.car 	= Car()
		self.car.name 	= str(name)
		self.car.color 	= str(color)
		self.car.price 	= float(price)

	def build(self):
		return Car(self)

car = CarBuilder("MyCar","Blue",10.2).build()

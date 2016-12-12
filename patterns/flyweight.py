""" Flyweight pattern applied to Python by martincastro.10.5@gmail.com """
class Order: 

	class Menu:

		elements = {} 

		class Food:
		
			def __init__(self,name):
				print "Creating expensive food: %s" % name
				self.name = name 
		
			def __str__(self):
				return "Food %s" % self.name

		@classmethod
		def get(cls,name):
			if not name in cls.elements:
				cls.elements[name] = cls.Food(name)
			return cls.elements[name]	

	menu = Menu()
	
	def __init__(self,amount,name):
		self.amount = amount
		self.food = self.__class__.menu.get(name)

o1 = Order(10,"Apples")
o2 = Order(10,"Oranges")
o3 = Order(10,"Apples")
o4 = Order(10,"Apples")

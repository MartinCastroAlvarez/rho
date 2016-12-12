""" Abstract Factory pattern applied to Python by martincastro.10.5@gmail.com """
class MyAbstractFactory: 

	@classmethod
	def getFactory(cls,type): 
		if type == "car": 	
			return Car()
		if type == "house": 
			return House()
		assert False, "Fail!"

	def buy(self): 
		pass

	def sell(self): 
		pass

class Car: 

	def __init__(self):
		print "Car created! User does now know the class name."
 
class House:

	def __init__(self):
		print "House created! User does now know the class name."

myarray = [] 
myarray.append( MyAbstractFactory.getFactory("car") )
myarray.append( MyAbstractFactory.getFactory("car") )
myarray.append( MyAbstractFactory.getFactory("house") )

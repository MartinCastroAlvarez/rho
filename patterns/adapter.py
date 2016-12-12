""" Adapter pattern applied to Python by martincastro.10.5@gmail.com """
class Fuel:

	def __init__(self,name):
		self.name = name

class Car:

	def __init__(self,name,fuel):
		self.name = name
		self.fuel = fuel

	def run(self):
		print "Running Car '%s' on fuel '%s'" % ( 
				self.name, self.fuel.getName() )

fuel = Fuel("Oil")
car = Car("Ferrari",fuel)
# car.run()				# Traceback (most recent call last):
					# File "<stdin>", line 1, in <module>
					# File "<stdin>", line 6, in run
					# AttributeError: Fuel instance has no attribute 'getName'
class FuelAdapter:

	def __init__(self,fuel):
		self.name = fuel.name

	def getName(self):
		return self.name

fuel = Fuel("Oil") 
adapter = FuelAdapter(fuel)
car = Car("Ferrari",FuelAdapter(fuel))
car.run()				# Running Car 'Ferrari' on fuel 'Oil'

""" Composite Pattern applied to Python by martincastro.10.5@gmail.com """
class Transport:

	def __init__(self):
		print "Creating means of transport..."
	
	def run(self):
		print "Running transport"

class Car(Transport): 

	def __init__(self):
		print "Creating a car..."
			
	def paint(self):
		print "Painint this car..."

class CarGroup(Transport):
	
	def __init__(self):
		self.children = []

	def add(self,c):
		assert isinstance(c,Car), "Not a Car Instance"
		self.children.append(c) 

	def paint(self):
		map( lambda x:x.paint(), self.children )


print "Managing instances separatedly..."
c1 = Car() 
c1.run()
c2 = Car() 
c2.run()
c3 = Car() 
c3.run()

print "Managing instanes together..."
cg = CarGroup()
cg.add(Car())
cg.add(Car())
cg.add(Car())
cg.paint()

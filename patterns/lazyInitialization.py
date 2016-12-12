""" Lazy Initialization applied to Python by martincastro.10.5@gmail.com """
class Person:
	created = {}    
	def __init__(self,name):
		self.name = name
	@classmethod
	def getElementByName(cls,name):
		if name not in cls.created:
			print "Creating class on demand."
			cls.created[name] = Person(name)
		return cls.created[name]                
	@classmethod
	def show(cls):
		for p in cls.created:
			print cls.created[p].name

print "Starting application fast."
a = Person.getElementByName("iron") 		# Creating class on demand.
Person.show() 					# iron
b = Person.getElementByName("maiden") 		# Creating class on demand.
Person.show() 					# maiden
						# iron
c = Person.getElementByName("iron")
Person.show() 					# maiden
						# iron

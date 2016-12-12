""" Multiton applied to Python by martincastro.10.5@gmail.com """
class Girl:
	instances = {}
	def __init__(self,name):
		if name in self.__class__.instances:
			print "Element already created"
			self = self.__class__.instances[name]
		else:
			print "Creating element..."
			self.name = name
		self.__class__.instances[name] = self

g = Girl("Sasha") 		# Creating element...
h = Girl("Avril") 		# Creating element...
i = Girl("Sasha") 		# Element already created


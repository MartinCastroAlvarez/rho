class Father:
	
	def view(self):
		print "This is the father"

class Child(Father):

	def view(self):
		print "This is the child"
		self.__class__.__bases__[0].view(self)

Child().view()

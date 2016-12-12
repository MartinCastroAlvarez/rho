class MyClass: 
	a = 3
	def __init__(self):
		self.b = 4

a = MyClass()
print dir(a)		# ['__doc__', '__init__', '__module__', 'a', 'b']

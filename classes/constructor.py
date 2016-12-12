class MyClass:

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __del__(self):
		print "Destroying object..."

bob = MyClass("bob",23) 
print bob.age			# 23
bob = None			# Destroying object

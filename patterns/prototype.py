""" Prototype applied to Python by martincastro.10.5@gmail.com """
import copy
class Room:
	class MyExpensiveObject:
		def __init__(self):
			print "Creating an expensive object"
	instance = MyExpensiveObject()
	@classmethod
	def getInstance(cls):
		return copy.deepcopy(cls.instance)
# Creating an expensive object
o = Room.getInstance()
p = Room.getInstance()
q = Room.getInstance()

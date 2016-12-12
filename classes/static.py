class Obj(object):
	instances = 0
	def __init__(self):
		self.__class__.instances += 1
	@staticmethod
	def getCount():
		print Obj.instances

o = Obj()
o = Obj()
o = Obj()
Obj.getCount()		# 3

class Obj(object):
	instances = 0
	def __init__(self):
		self.__class__.instances += 1
	@classmethod
	def getCount(cls):
		print cls.instances

o = Obj()
o = Obj()
o = Obj()
Obj.getCount()		# 3

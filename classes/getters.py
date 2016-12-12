class Flight:

	def __init__(self):
		self.x = int()
		self.setTime(1000)

	def getTime(self):
		if self.x > 0:
			return self.x
		else:
			return 0

	def setTime(self,x):
		self.x = int(x)

f = Flight()
print f.getTime()		# 1000
f.setTime(10.2)
print f.getTime() 		# 10

""" Momento pattern applied to Python by martincastro.10.5@gmail.com """
import copy

class Metallica:
	
	def __init__(self,a=0,b=0,c=0):
		self.setA(a)
		self.setB(b)
		self.setC(c)

	def __str__(self):
		return "a=%i b=%i c=%i" % (self.a,self.b,self.c)

	def setA(self,x=0):
		self.a = int(x)

	def getA(self):
		return self.a

	def setB(self,x=0):
		self.b = int(x)

	def getB(self):
		return self.b

	def setC(self,x=0):
		self.c = int(x)

	def getC(self):
		return self.c

	def getSavedInstance(self):
		m = self.__class__()
		m.setA(self.getA())
		m.setB(self.getB())
		m.setC(self.getC())
		return m

	def restoreFromSavedState(self,m):
		self.setA(m.getA())	
		self.setB(m.getB())	
		self.setC(m.getC())	
	
m = Metallica()
m.setA(1)
m.setB(2)
m.setC(3)
print m
s = m.getSavedInstance()
m.setB(4)
print m
m.restoreFromSavedState(s)
print m

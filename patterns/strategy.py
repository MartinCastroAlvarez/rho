""" Strategy pattern applied to Python by martincastro.10.5@gmail.com """

class Strategy:

	def add(self,x):
		raise Exception("Not implemented") 

class NormalStrategy(Strategy):
	
	def add(self,x,p):
		return (x,float(p))

class HappyHourStrategy(Strategy):
	
	def add(self,x,p):
		return (x,float(p)*0.5)

class Client:
	
	def __init__(self,name):
		self.name = name
		self.queue = [] 
		self.happyHourOff()

	def setStrategy(self,s):
		assert isinstance(s,Strategy), "Invalid instance class"
		self.strategy = s

	def happyHourOn(self):
		self.setStrategy(HappyHourStrategy())

	def happyHourOff(self):
		self.setStrategy(NormalStrategy())

	def add(self,x,p):
		self.queue.append(self.strategy.add(x,p))

	def bill(self):
		total = 0 
		print "Client %s" % self.name
		print "-------------------"
		for q in self.queue:
			total += q[1]
			print "%-10s $ %5.2f" % (q[0],q[1])
		print "-------------------"
		print "%-10s $ %5.2f" % ("Total",total)

a = Client("a")
a.add("Beer",10)
a.add("Beer",10)
a.add("Beer",10)
a.happyHourOn()
a.add("Beer",10)
a.add("Beer",10)
a.bill()

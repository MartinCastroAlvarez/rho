""" Chain of responsability applied to Python by martincastro.10.5@gmail.com """

class Request:

	def __init__(self,severity,description):
		self.sev = int(severity)
		self.desc = description

	def getPriority(self):
		return self.sev	

	def __str__(self):
		return "SEV %i - %s" % ( self.sev, self.desc ) 

class BusinessTree:

	def setBoss(self,e):
		assert isinstance(e,BusinessTree), "Not a BusinessTree object!"
		self.boss = e

	def evaluate(self,r):
		assert isinstance(r,Request), "Not a valid request"
		print "Evaluating %s" % r

class TeamLeader(BusinessTree):

	def evaluate(self,r):
                self.__class__.__bases__[0].evaluate(self,r)
		if r.getPriority() == 3:
			print "Managed by TeamLeader!"
		else:
			print "Not Managed by TeamLeader..."
			self.boss.evaluate(r)

class Manager(BusinessTree):

	def evaluate(self,r):
                self.__class__.__bases__[0].evaluate(self,r)
		if r.getPriority() == 2:
			print "Managed by Manager!"
		else:
			print "Not Managed by Manager..."
			self.boss.evaluate(r)
	
class President(BusinessTree):

	def evaluate(self,r):
                self.__class__.__bases__[0].evaluate(self,r)
		if r.getPriority() == 1:
			print "Managed by President!"
		else:
			print "Not Managed by anybody..."
	
p1 = President()
p2 = Manager()
p2.setBoss(p1) 
p3 = TeamLeader()
p3.setBoss(p2) 

p3.evaluate( Request(3,"This a minor problem...") )
p3.evaluate( Request(2,"This a normal problem...") )
p3.evaluate( Request(1,"This a Serious problem...") )

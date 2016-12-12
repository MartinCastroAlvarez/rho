""" Pool Method applied to Python by martincastro.10.5@gmail.com """
import time
class DBConnection:
	DBS     = []
	POOL    = 5

	class MyConnection:
		def __init__(self):
               		self.available = True

	@classmethod
	def initPool(cls):
		while len(cls.DBS) < cls.POOL:
			db = cls.MyConnection()
			cls.DBS.append(db)
	@classmethod
	def getInstance(cls):
		i = 0
		while i < len(cls.DBS) and not cls.DBS[i].available:
			i += 1
			if i == cls.POOL:
				i = 0
				time.sleep(5)
		cls.DBS[i].available = False
		return cls.DBS[i]

	@classmethod
	def releaseInstance(cls,db):
		i = 0
		while i < len(cls.DBS) and id(cls.DBS[i]) == id(db):
			i += 1
		cls.DBS[i].available = True
	@classmethod
	def printStatus(cls):
		for db in cls.DBS:
			print "Database: %-20.0i Available: %r" % ( id(db), db.available ) 

DBConnection.initPool()
a = DBConnection.getInstance()
b = DBConnection.getInstance()
c = DBConnection.getInstance()
DBConnection.printStatus() 		# Database: 139808686394112      Available: False
					# Database: 139808686392960      Available: False
					# Database: 139808686392600      Available: False
					# Database: 139808686393320      Available: True
					# Database: 139808686394328      Available: True
DBConnection.releaseInstance(c)
DBConnection.printStatus() 		# Database: 139808686394112      Available: True
					# Database: 139808686392960      Available: False
					# Database: 139808686392600      Available: False
					# Database: 139808686393320      Available: True
					# Database: 139808686394328      Available: True

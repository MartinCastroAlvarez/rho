""" Balking pattern applied to Python by martincastro.10.5@gmail.com """

import threading
import time

class MyThread(threading.Thread):
	
	def __init__(self,id):
		threading.Thread.__init__(self)
		self.id = id
		self.isOFF = True

	def changeStatus(self):
		self.isOFF = False

	def run(self):
		print "Starting Thread-%i" % self.id
		for i in range(0,10):
			if self.isOFF:
				print "Thread-%i is OFF" % self.id
			else:
				print "Thread-%i is ON" % self.id
			time.sleep(3)
		print "Exiting Thread-%i" % self.id

t1 = MyThread(1)

t1.start()

print "Waiting at main thread"
time.sleep(5)
t1.changeStatus()

print "End of main thread"

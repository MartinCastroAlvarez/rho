""" Binding pattern applied to Python by martincastro.10.5@gmail.com """

import threading
import time

class MyThread(threading.Thread):

	binded_property = True
	
	def __init__(self,id):
		threading.Thread.__init__(self)
		self.id = id

	def run(self):
		print "Starting Thread-%i" % self.id
		v = self.__class__.binded_property
		while v:
			time.sleep(3)
			v = self.__class__.binded_property
		print "Exiting Thread-%i" % self.id

t1 = MyThread(1)
t2 = MyThread(2)

t1.start()
t2.start()

print "Waiting at main thread"
time.sleep(5)
MyThread.binded_property = False

print "End of main thread"

import threading
import time

class MyThread(threading.Thread):
	
	def __init__(self,id,counter):
		threading.Thread.__init__(self)
		self.id = id
		self.counter = counter

	def run(self):
		print "Starting Thread-%i" % self.id
		for i in range(0,self.counter):
			print "Working at Thread-%i" % self.id
			time.sleep(2)
		print "Exiting Thread-%i" % self.id

t1 = MyThread(1,10)
t2 = MyThread(2,5)

t1.start()
t2.start()

print "End of main thread"

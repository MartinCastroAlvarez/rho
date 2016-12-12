import threading
import Queue
import time

class MyThread(threading.Thread):
	
	lock = threading.Lock()
	queue = Queue.Queue(10)

	@classmethod
	def addQ(cls,x):
		cls.lock.acquire()
		cls.queue.put(x)
		cls.lock.release()
	
	def __init__(self,id,counter):
		threading.Thread.__init__(self)
		self.id = id	
		self.counter = counter

	def run(self):
		print "Starting Thread-%i" % self.id 	
		while not self.__class__.queue.empty():
			self.__class__.lock.acquire()
			my_elem = self.__class__.queue.get()
			self.__class__.lock.release()
			print "Thread-%i working on %s" % (self.id,my_elem)
			time.sleep(self.counter)
		print "Exiting Thread-%i" % self.id 	

t1 = MyThread(1,4)
t2 = MyThread(2,2)

MyThread.addQ("Jazz")
MyThread.addQ("Blues")
MyThread.addQ("Rock")
MyThread.addQ("Electro")
MyThread.addQ("Salsa")
MyThread.addQ("Tap")
MyThread.addQ("Metal")
MyThread.addQ("Trash Metal")

t1.start()
t2.start()

print "Waiting for all thread to complete..."
t1.join()
t2.join()

print "End of main thread"

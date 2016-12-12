""" Binding pattern applied to Python by martincastro.10.5@gmail.com """

import threading
import Queue
import time

class Message:
	
	def __init__(self,text):
		self.text = text

class MyThread(threading.Thread):
	
	MQ = Queue.Queue(10)
	lock = threading.Lock()

	@classmethod
	def addMessage(cls,text):
		cls.MQ.put(text)

	def __init__(self,id):
		threading.Thread.__init__(self)
		self.id = id

	def checkMessages(self):
		m = None
		self.__class__.lock.acquire()
		if not self.__class__.MQ.empty(): 
			m = self.__class__.MQ.get()
		self.__class__.lock.release()
		if m:
			print "Thread-%i reads: %s" % (self.id,m)

	def run(self):
		print "Starting Thread-%i" % self.id
		for i in range(0,10):
			self.checkMessages()
			if i == self.id * 2:
				self.__class__.addMessage("Thread-%i says hi!" % self.id)
			time.sleep(3)
		print "Exiting Thread-%i" % self.id

t1 = MyThread(1)
t2 = MyThread(2)
t3 = MyThread(3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print "End of main thread"

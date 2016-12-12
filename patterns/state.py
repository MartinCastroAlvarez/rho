""" State pattern applied to Python by martincastro.10.5@gmail.com """

class WormState:

	def __init__(self):
		self.name = "Worm"
	
	def action(self):
		print "The worm has started to crawl..."

class ButterflyState:

	def __init__(self):
		self.name = "Butterfly"
	
	def action(self):
		print "The butterfly has started to fly!"

class Worm:

	def __init__(self):
		self.state = WormState()

	def action(self):
		self.state.action()

	def evolve(self):
		self.state = ButterflyState()


w = Worm()
w.action()
w.evolve()
w.action()

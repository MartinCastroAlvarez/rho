""" Factory Method applied to Python by martincastro.10.5@gmail.com """

class Game:

	def play(self):
		print self.getMap()

	def getMap(self):
		pass

class EasyGame(Game):  

	def getMap(self):
		return "This is an easy map..."

class HardGame(Game):  

	def getMap(self):
		return "This is a really HARD map!!"

e = EasyGame()
e.play() 			# This is an easy map...
h = HardGame()
h.play() 			# This is a really HARD map!!

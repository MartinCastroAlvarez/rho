""" Template pattern applied to Python by martincastro.10.5@gmail.com """

class SongTemplate: 

	def __init__(self):
		self.end = False

	def songIsNotOver(self):
		return not self.end

	def playSong(self):
		print ""
		self.title()
		print ""
		while self.songIsNotOver():
			self.play()
		print ""

class StairwayToHeaven(SongTemplate):

	def title(self):
		print "Stairway to Heaven - Led Zepelin"

	def play(self):
		print "And as we wind on down the road"	
		print "Our shadows taller than our soul."
		print "There walks a lady we all know"
		print "Who shines white light and wants to show"
		print "How everything still turns to gold."
		print "And if you listen very hard"
		print "The tune will come to you at last."
		print "When all are one and one is all"
		print "To be a rock and not to roll."
		self.end = True

class GoodbyeBlueSky(SongTemplate):

	def title(self):
		print "Goodbye Blue Sky - Pink Floyd"

	def play(self):
		print "Oooooooo ooo ooo ooooh"
		print "Did you see the frightened ones"
		print "Did you hear the falling bombs"
		print "Did you ever wonder"
		print "Why we had to run for shelter"
		print "When the promise of a brave new world"
		print "Unfurled beneath a clear blue sky"
		self.end = True

sth = StairwayToHeaven()
sth.playSong()
gbs = GoodbyeBlueSky()
gbs.playSong()

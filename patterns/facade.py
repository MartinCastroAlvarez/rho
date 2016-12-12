""" Facade Pattern applied to Python by martincastro.10.5@gmail.com """
class Guitar:
	
	def __init__(self):
		print "Adding a lead guitar to the band"

	def play(self):
		print "Playing a Am"

class Bass:
	
	def __init__(self):
		print "Adding a bass to the band. A Guitar is needed."

	def play(self):
		print "Playing a G#"

class Drums:
	
	def __init__(self):
		print "Adding drums to the band. A Bass an Drums are needed."

	def play(self):
		print "Playing a Fmaj7"

class Band:

	def __init__(self):
		print """ Adding instruments in a certain 
			order that the user might not be aware of """
		self.guitar = Guitar()
		self.bass = Bass()
		self.drums = Drums()

	def play(self):
		self.guitar.play()	
		self.bass.play()	
		self.guitar.play()	
		self.drums.play()	
		self.guitar.play()	
	
b = Band()
b.play()

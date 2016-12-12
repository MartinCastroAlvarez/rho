class Song:
	
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return self.name

s = Song("Louder than words") 
print s				# Louder than words

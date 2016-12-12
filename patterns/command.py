""" Command pattern applied to Python by martincastro.10.5@gmail.com """

class Light: 
	
	def __init__(self):
		self.isON = False

class Command: 

	def turnON(self,e):
		assert isinstance(e,Light), "Not a Light instance!"
		print "Turning ON"
		e.isON = True

	def turnOFF(self,e):
		assert isinstance(e,Light), "Not a Light instance!"
		print "Turning OFF"
		e.isON = False

	def switch(self,e):
		assert isinstance(e,Light), "Not a Light instance!"
		if e.isON: 
			self.turnOFF(e)
		else:
			self.turnON(e)

led_lamp = Light()
flash_light = Light()
oil_lamp = Light()

c = Command()

c.turnON(led_lamp)
c.turnOFF(flash_light)
c.switch(oil_lamp)
c.switch(oil_lamp)
c.switch(oil_lamp)
c.switch(oil_lamp)

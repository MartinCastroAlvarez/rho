""" LooseCoupling & Mediator pattern applied to Python by martincastro.10.5@gmail.com """

class Executable:

	def execute(self):
		raise Exception("Not implemented")
	
class Title(Executable): 
	
	def __init__(self,med):
		self.mediator = med	
		self.mediator.registerTitle(self)
	
	def execute(self):
		print("Title!")
	
class Subitle(Executable): 
	
	def __init__(self,med):
		self.mediator = med	
		self.mediator.registerSubtitle(self)

	def execute(self):
		print("Subtitle!")
	
class View(Executable): 
	
	def __init__(self,med):
		self.mediator = med	
		self.mediator.registerView(self)
	
class Mediator:
	
	def __init__(self):
		self.h1 = None;
		self.h2 = None;
		self.view = None

	def registerTitle(self,h1):
		assert isinstance(h1,Executable), "Not a valid instance!"
		self.h1 = h1

	def registerSubtitle(self,h2):
		assert isinstance(h2,Executable), "Not a valid instance!"
		self.h2 = h2

	def registerView(self,view):
		assert isinstance(view,Executable), "Not a valid instance!"
		self.view = view

mediator = Mediator()
title	 = Title(mediator)
subtitle = Subitle(mediator)
view	 = View(mediator)

mediator.h2.execute()
mediator.h1.execute()

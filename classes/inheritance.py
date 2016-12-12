class MyFather: 
	def __init__(self,name,age): 
		self.name = name 
		self.age = age 

class MyOtherFather: 
	def getName(self):
		return self.name

class MyChild(MyFather, MyOtherFather):
	def getAge(self):
		return self.age
	pass 

rob = MyChild('rob',29)
print rob.age 			# 29
print rob.getName()		# rob

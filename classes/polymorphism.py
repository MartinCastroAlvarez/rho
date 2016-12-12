class MyFather: 
	def compare(self,myint): 
		return myint>=1

class MyChild(MyFather): 
	def getAge(self):
		return 3

arr = [ 
	MyFather(), 
	MyChild(),
] 
for a in arr: 
	print a.compare(3)		# True
					# True

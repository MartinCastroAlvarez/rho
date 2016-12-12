""" Binary Tree applied to Python by martincastro.10.5@gmail.com """

class Comparable: 

	def compare(self, e):
		pass 	

class BinaryTree: 

	class TreeNode:

		def __init__(self):
			self.me 	= None 
			self.left 	= None	
			self.right 	= None
			
		def __add__(self,e):
			assert isinstance(e,Comparable), "Element is not Comparable!"
			if not self.me:
				print "Added '%s'!" % e
				self.me = e
			else: 
				if self.me.compare(e)<0:
					print "Adding '%s' to the LEFT..." % e
					if not self.left:
						self.left = self.__class__()
					self.left.__add__(e)
				else:
					print "Adding '%s' to the RIGHT..." % e
					if not self.right:
						self.right = self.__class__()
					self.right.__add__(e)

		def __search__(self,e):
			assert isinstance(e,Comparable), "Element is not Comparable!"
			results = []
			if self.me: 
				c = self.me.compare(e)
				if c == 0: 	
					results.append(self.me) 
				if c<0 and self.left: 
					for e in self.left.__search__(e):
						results.append(e)
				if c>=0 and self.right: 
					for e in self.right.__search__(e):
						results.append(e)
			return results

	def __init__(self):
		self.root = self.TreeNode()

	def add(self,e):
		self.root.__add__(e)

	def search(self,e):
		return self.root.__search__(e)

	def delete(self,e):
		print """ This method is good for storing large & 
			comparable objects that will not be deleted! """
	
class Order(Comparable):
	
	def __init__(self,amount,name):
		self.name = name
		self.amount = int(amount)

	def __str__(self):
		return "%i %s" % (self.amount,self.name)

	def compare(self,e):
		assert isinstance(e,Order), "Element is not an Order"
		return e.amount - self.amount
			

tree = BinaryTree()
tree.add( Order(3,"Guitars") )
tree.add( Order(1,"Bass") )
tree.add( Order(2,"Drums") )
tree.add( Order(4,"Microphones") )
tree.add( Order(7,"Saxophones") )
tree.add( Order(3,"Keyboards") )
tree.add( Order(1,"Flute") )

print "Searching..."
for e in tree.search( Order(3,"Keyboards") ):
	print e

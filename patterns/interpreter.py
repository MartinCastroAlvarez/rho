""" Interpreter pattern applied to Python by martincastro.10.5@gmail.com """
class Symbol:

	def eval(self,left,right):
		raise NotImplementedError	
	
class Plus(Symbol):

	def evaluate(self,left,right):
		return left.evaluate() + right.evaluate()

class Minus(Symbol):

	def evalauate(self,left,right):
		return left.evaluate() - right.evaluate()

class Multiply(Symbol):

	def evaluate(self,left,right):
		return left.evaluate() * right.evaluate()

class Divide(Symbol):

	def evaluate(self,left,right):
		return left.evaluate() / right.evaluate()

class Number:

	def __init__(self,n):
		self.n = float(n)
	
	def evaluate(self):
		return self.n

class TreeNode:

	symbols = [ 
		[ "*", Multiply, ],
		[ "+", Plus, 	 ],
		[ "-", Minus,	 ],
		[ "/", Divide, 	 ], 
	] 

	def __init__(self,expr,):
		self.me 	= None
		self.left 	= None
		self.right 	= None
		left_expr 	= ""
		right_expr 	= ""
		for e in expr:
			if self.me: 
				right_expr += e
			else: 
				left_expr += e 
				for s in self.__class__.symbols: 
					if e == s[0]:
						self.me = s[1]()
		if not self.me: 
			self.me = Number(expr)
		left_expr = left_expr[:-1] 
		if len(left_expr)>0:
			self.left = TreeNode(left_expr)
		if len(right_expr)>0:
			self.right = TreeNode(right_expr)

	def evaluate(self): 
		if isinstance(self.me, Symbol):
			return self.me.evaluate(self.left, self.right)
		if isinstance(self.me, Number):
			return self.me .evaluate()
		else:
			return 0

class Interpreter:
	
	def __init__(self,expr):
		self.expr = expr
		self.tn = TreeNode(expr)	
		
	def view(self):
		r = self.tn.evaluate()
		print "%s = %.2f" % (self.expr,r)

Interpreter("1+1").view()
Interpreter("2+3*4").view()
Interpreter("1*5").view()
Interpreter("10/2").view()

class A:
        pass

class B(A):
        pass

class C:
	pass

class D(A,C):
	pass

e = D()
print isinstance(e,A) 		# True
print isinstance(e,B) 		# False
print isinstance(e,C) 		# True
print isinstance(e,D) 		# True

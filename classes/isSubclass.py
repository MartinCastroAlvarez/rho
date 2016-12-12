class A:
        pass

class B(A):
        pass

class C:
	pass

class D(A,C):
	pass

print issubclass(D, A) 		# True
print issubclass(D, B) 		# False
print issubclass(D, C) 		# True
print issubclass(D, D) 		# True

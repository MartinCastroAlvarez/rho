mytuple = (1,2,3,4,5,6)
print list(mytuple) 		# [1, 2, 3, 4, 5, 6]
print tuple(mytuple) 		# (1, 2, 3, 4, 5, 6)
mytuple[4] = 4 			# Traceback (most recent call last):
 				# File "<stdin>", line 1, in <module>
				# TypeError: 'tuple' object does not support item assignment

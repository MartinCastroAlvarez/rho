a = 1 
assert a == 1 
assert a == 2, "Failed here!" 		# Traceback (most recent call last):
					# File "<stdin>", line 1, in <module>
					# AssertionError: Failed here!
assert False, "Always fail!"		# Traceback (most recent call last):
					# File "<stdin>", line 1, in <module>
					# AssertionError: Always fail!

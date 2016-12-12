try:
	raise Exception("My Exception")
except ValueError as e:
	print "ValueError: " + e.__str__()
except TypeError as e:
	print "TypeError: " + e.__str__()
else:
	print "Not any Exception raised!"
finally:
	print "Finally"

try:
	a = 3
except:
	print "Exception"
else:
	print a 
	print "Not any Exception raised!"
finally:
	print "Finally"

try:
	raise NotImplementedError("My Error")
except (NameError,TypeError) as e:
	print "Except: " + e.__str__()
else:
	print "Else"
finally:
	print "Finally"

raise ZeroDivisionError				# ZeroDivisionError: integer division or modulo by zero
raise NameError					# NameError: name 'spam' is not defined
raise TypeError					# TypeError: cannot concatenate 'str' and 'int' objects
raise IOError
raise ValueError				# ValueError: Could not convert data to an integer.
raise Exception					# Exception
raise NotImplementedError

class MyError(Exception):

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

s = "Bob Smith"
print list(s)						# ['B', 'o', 'b', ' ', 'S', 'm', 'i', 't', 'h']
print tuple(s)						# ('B', 'o', 'b', ' ', 'S', 'm', 'i', 't', 'h')
print s.split() 					# ['Bob', 'Smith']
print s.split("b") 					# ['Bo', ' Smith']
print type("asdf") 					# <type 'str'>
print("my text: %20.15s" % "long_string_more_than_15")  # my text:      long_string_mor
print "asdf" * 2 					# 'asdfasdf'
s = "Avril Lavigne" 				
print s[::-1] 						# 'engivaL lirvA'
print str()						# ''
s = "Soda"
print s.upper() 					# 'SODA'
print s.lower() 					# 'soda'
print ord("a")						# 97
print [ord(c) for c in "Gilmour"]			# [71, 105, 108, 109, 111, 117, 114]
for e in "Pink": print e, 				# P i n k
s = "RemoveLast" 
print s[:-1] 				 		# RemoveLas

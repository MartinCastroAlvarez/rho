i = 0 
mylist = [ 1, 2, 3, 4, ] 
while i<len(mylist): 
	print mylist[i], 
	i += 1 					# 1 2 3 4
for i in mylist: print i, 			# 1 2 3 4
print [i for i in mylist] 			# [1,2,3,4]
print map(lambda x: x, mylist) 			# [1,2,3,4]
print map(lambda x: x<3, mylist)		# [True,True,False,False]
print filter(lambda x: x<2, mylist)		# [1] 

i = iter([1,2,3,4])
print type(i)					# <type 'listiterator'>
print i.next() 					# 1
print i.next() 					# 2
print i.next() 					# 3
print i.next() 					# 4
print i.next() 					# Traceback (most recent call last):
						# File "<stdin>", line 1, in <module>
						# StopIteration

def lazy():
	for x in range(0, 10):
		yield x

mylist = ['Bob Smith', 42, 30000, 'software']
print mylist[0] 				# 'Bob Smith'
print mylist[1] 				# 42
print mylist[-1]				# 'software'
print mylist[-2]				# 30000
print mylist[0:2]				# ['Bob Smith', 42]
print mylist[0:4:2]				# ['Bob Smith', 30000]
print mylist[0::2]				# ['Bob Smith', 30000]
print mylist[:3] 				# ['Bob Smith', 42, 30000]
print mylist[1:-1] 				# [42, 30000]
mylist.append(1)
print mylist 					# ['Bob Smith', 42, 30000, 'software', 1]
print mylist.pop() 				# 1
print mylist 					# ['Bob Smith', 42, 30000, 'software']
mylist = [ 1, 2, 3 , 4 ]
print len(mylist)				# 4
print sum(mylist)				# 10
mylist.reverse()
print mylist					# ['software', 30000, 42, 'Bob Smith']

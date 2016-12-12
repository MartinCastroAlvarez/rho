mydict = { "a":1, "b":2, "c":3, } 
mydict = dict(a=1,b=2,c=3)
print mydict['a'] 							# 1
print mydict.items()							# [('a', 1), ('c', 3), ('b', 2)]
print mydict.keys() 							# ['a', 'c', 'b']
print mydict.values() 							# [1, 3, 2]
for i in mydict: mydict[i] 						# 1
									# 2 
									# 3 
print map(lambda x:mydict[x], mydict) 					# [1, 3, 2]
print filter(lambda x:mydict[x]>1, mydict) 				# ['c', 'b']
print map(lambda x:mydict[x], filter(lambda x:mydict[x]>1, mydict))	# [3, 2]
print len(mydict) 							# 3
print mydict.get("a") 							# 1
print mydict.has_key("d") 						# False
print mydict.pop("c") 							# 3
import pprint
mydict = dict(a=1,b=2,c=[1,3,4])
print mydict 								# {'a': 1, 'c': [1, 3, 4], 'b': 2}
pprint.pprint(mydict) 							# {'a': 1, 'b': 2, 'c': [1, 3, 4]}

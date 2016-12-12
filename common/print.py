myvar1 = 1
myvar2 = 2
print(myvar1, myvar2) 				# 1 2
print(myvar1, "\n", myvar2) 			# 1 
						# 2
print(myvar1, "\t", myvar2) 			# 1 	2
print("""
	Long text that spans
	more than one single line 
""")
print("background", "\r", "top") 		# topkground 
print("%30.10s" % "my_long_text") 		# my_long_te
print("%-.3i" % 2) 				# 002
print("%10.5f" % 7.5) 				# 7.50000
print("%3.3r" % False) 				# Fal

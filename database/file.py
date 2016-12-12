
""" Write to file """
myfile = open("/tmp/test.txt","w") 
type(myfile) # <type 'file'>
myfile.write("MY TEXT\n") 
myfile.close()

""" Append to file """
myappend = file("/tmp/test.txt","a") 
myappend.write("Another brick in the wall\n") 
myappend.close()

""" Read file """
myread = open("/tmp/test.txt","r")
for line in myread.read().split("\n"): print line # MY TEXT
myread.close()

""" Read one line at a time """
import fileinput
for line in fileinput.input(['/tmp/test.txt']):
    print line

""" Replace one line """
myfile = open("/tmp/test.txt","w") 
myfile.seek(3)
myfile.write("MY TEXT\n") 
myfile.close()

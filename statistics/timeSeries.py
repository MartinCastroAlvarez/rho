#!/usr/bin/python
import numpy
import random
from scipy import stats
import matplotlib.pyplot as plt

# App Logic.
s = numpy.genfromtxt("./csv/BJsales.csv",delimiter=',',usecols=[1,2],skip_header=0,names=True)
y = s['BJsales'] 
x = s['time'] 
r,p,r_value,p_value,err = stats.linregress(x,y)
corr = numpy.corrcoef(x,y)[0][1]

# View.
for i in range(0,10):
	print "%s" % s[i]
print "..."
print "Correlation: %.2f" % corr
print "Linear Regression: y=%.2f+%.2fx " % (p,r)

print "%12.12s %12.12s %12.12s" % ("Index","Real","Proyection") 
for i in [1,5,10,25,50,100,150,200,1000]:
	try: 
		yreal = y[i]
	except:
		yreal = 0 
	ytest = p+i*r
	print "%12.2f %12.2f %12.2f" % (i,yreal,ytest)

# Graphics.
trend = p+r*x
plt.scatter(x,y)
plt.plot(x,trend)
plt.show()

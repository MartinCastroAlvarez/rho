#!/usr/bin/python
import scipy.stats
import matplotlib.pyplot as plt
import numpy
import math
SIZE = 50

PURPLE          = '\033[95m'
CYAN            = '\033[96m'
DARKCYAN        = '\033[36m'
BLUE            = '\033[94m'
GREEN           = '\033[92m'
YELLOW          = '\033[93m'
RED             = '\033[91m'
BOLD            = '\033[1m'
UNDERLINE       = '\033[4m'
END             = '\033[0m'

print 
print BOLD+CYAN+"Normal distribution"+END
MEAN  = 10
VAR   = 2
print "Everybody takes in average %.2f minutes to complete a transaction with a variance of %.2f." % (MEAN,VAR)
nm = scipy.stats.norm.rvs(size=SIZE,loc=MEAN,scale=VAR)
print nm
print "Average is set to: %.2f" % MEAN
print "Average is really: %.2f" % (sum(nm)/float(SIZE))
for x in [1,4,7,9,10,11,15,19]:
	print "The probabilty of taking %i seconds is: %.2f" % (x,scipy.stats.norm.pdf(x,loc=MEAN,scale=VAR)) 
ALPHA = 0.05
for x in [1,9,10,11,30,50]:
	tstud,pvalue = scipy.stats.ttest_1samp(nm,x)
	if pvalue < ALPHA:
		print "Does the t-student test considers %i as the mean of the population? NO" % x
	else: 
		print "Does the t-student test considers %i as the mean of the population? yes!" % x
"""
plt.plot(range(0,SIZE),nm)
plt.show()
"""

print 
print BOLD+CYAN+"Bernoulli distribution"+END
PROB = 0.2
br = scipy.stats.bernoulli.rvs(PROB,size=SIZE)
print br
print "Probability of True is set to: %.2f" % PROB
print "Probability of True is really: %.2f" % (sum(br)/float(SIZE))
"""
plt.plot(range(0,SIZE),br)
plt.show()
"""

print 
print BOLD+CYAN+"Binomial distribution"+END
PROB  = 0.5
TIMES = 25
print "Results of flipping a coin %i times with %.2f probability and winning."  % (TIMES,PROB)
bn = scipy.stats.binom.rvs(TIMES,PROB,size=SIZE)
print bn
print "Average number of flips won: %.2f" % (sum(bn)/float(SIZE))
for x in [0,1,3,5,7,9]:
	print "Probability of winning %i times in 10 flips: %.2f" % (x,scipy.stats.binom.pmf(x,10,PROB))

print 
print BOLD+CYAN+"Poisson distribution"+END
OCURRENCES = 2
TIMELAPSE  = 10
LAMBDA	   = float(OCURRENCES)/TIMELAPSE
print "Every %i boxes that are checked, there are %i elements found to be missing" % (TIMELAPSE,OCURRENCES)
ps = scipy.stats.poisson.rvs(LAMBDA,size=SIZE)
print ps
print "Average errors per box is set to: %.2f" % LAMBDA
print "Average errors per box is really: %.2f" % (sum(ps)/float(SIZE))
for x in range(0,4):
	print "The probability of finding %i missing objetcs is %.2f" % (x,scipy.stats.poisson.pmf(x,LAMBDA))
"""
plt.plot(range(0,SIZE),ps)
plt.show()
"""

print 
print BOLD+CYAN+"Hypergeometric distribution"+END
SAMPLE  = 20
SUCCESS = 7
SELECT  = 12
print "There are %i dogs in a collection of %i animals." % (SUCCESS,SAMPLE)
print "How many dogs will I find if I select %i random animals?" % SELECT
hg = scipy.stats.hypergeom.rvs(SAMPLE,SUCCESS,SELECT,size=SIZE)
print hg
print "Average is really: %.2f" % (sum(hg)/float(SIZE))
for x in [1,2,3,4,7,12,15]:
	print "The probability of selecting %i dogs is: %.2f" % (x,scipy.stats.hypergeom.pmf(x,SAMPLE,SUCCESS,SELECT))
"""
plt.plot(range(0,SIZE),hg)
plt.show()
"""

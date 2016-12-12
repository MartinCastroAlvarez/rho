#!/usr/bin/python
import csv, numpy

# SECTION I: Load data from csv datasource into numpy.
matrix = []
names = []
with open("csv/abortion.csv",'rb') as csvfile:
	for line in csv.reader(csvfile,delimiter=',',quotechar='"'):
		for i,col in enumerate(line):
			if i == 0:
				names.append((col,numpy.int))
			else:
				try: 
					matrix[i-1].append(int(col))
				except: 
					matrix.append([int(col)])
for i,row in enumerate(matrix):
	matrix[i] = tuple(row)
dt = numpy.dtype(names)
a = numpy.array(matrix,dtype=dt)

# SECTION II: Print statistics info.
stats = [] 
stats.append(["Maximum Abortion Rate", 				numpy.amax(a['TOTAL']) ])
stats.append(["Minimum Abortion Rate", 				numpy.amin(a['TOTAL']) ])
stats.append(["25 percentile of unmarried abortions",		numpy.percentile(a['UNMARRIED (IL RESIDENT)'],25) ])
stats.append(["50 percentile of unmarried abortions",		numpy.percentile(a['UNMARRIED (IL RESIDENT)'],50) ])
stats.append(["75 percentile of unmarried abortions",		numpy.percentile(a['UNMARRIED (IL RESIDENT)'],75) ])
stats.append(["Married abortions mean", 			numpy.mean(a['MARRIED (IL RESIDENT)']) ])
stats.append(["Married abortions median", 			numpy.median(a['MARRIED (IL RESIDENT)']) ])
stats.append(["Age 15-17 abortions mean", 			numpy.mean(a['Age 15-17']) ])
stats.append(["Age 15-17 abortions standard deviation", 	numpy.std(a['Age 15-17']) ])
stats.append(["Age 15-17 abortions variance", 			numpy.var(a['Age 15-17']) ])
stats.append(["Age 18-19/ Age 20-24 Correlation", 		numpy.corrcoef(a['Age 18-19'],a['Age 20-24'])[1][0] ])
stats.append(["Year/ Age 45 and Over Correlation", 		numpy.corrcoef(a['YEAR'],a['Age 45 and Over'])[1][0] ])
stats.append(["Age 15-17/ Age 30-34 covariance", 		numpy.cov(a['Age 15-17'],a['Age 30-34'])[0][0] ])

# SECTION II: View datatable.
print "\n ABORTION DEMOGRAPHICS \n"
for n in a.dtype.names:
	print "%8.8s" % n, 		
print 
for lines in a:
	for n in lines:
		print "%8.8s" % n, 
	print 
print "\n STATISTICS \n"
# print dt.names
for s in stats:
	print " %40.40s: %-8.8s" % (s[0],s[1])
print 

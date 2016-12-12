#!/usr/bin/python
import csv, numpy, random, math
import matplotlib.pyplot as plt

PRODUCTS 	= 15 
TOTAL_YEARS 	= 4
FIRST_YEAR 	= 2010

# Generate random matrix.
matrix_prices  = []
matrix_amounts = []
for p in range(0,PRODUCTS):
	row_prices  = [] 
	row_amounts = [] 
	for y in range(0,TOTAL_YEARS):
		col_prices = 0
		col_amounts = 0
		try: 
			col_prices  = row_prices[y-1]  + random.uniform(0,10)
			col_amounts = row_amounts[y-1] - random.randint(10,100)
		except:
			col_prices  = random.uniform(10,100)
			col_amounts = random.randint(500,3000)
		row_prices.append(col_prices)	
		row_amounts.append(col_amounts)	
	matrix_prices.append(row_prices)
	matrix_amounts.append(row_amounts)

# Calculate indexes.
matrix_indexes = {} 
for y in range(0,TOTAL_YEARS):
	mydict = {} 
	p,q = 0,0
	for i in range(0,PRODUCTS):
		p += matrix_prices[i][y] 
		q += matrix_prices[i][0] 
	mydict['simple'] = p/q
	p,q = 0,0
	for i in range(0,PRODUCTS):
		p += matrix_prices[i][y] * matrix_amounts[i][0]
		q += matrix_prices[i][0] * matrix_amounts[i][0]
	mydict['laspeyres'] = p/q
	p,q = 0,0
	for i in range(0,PRODUCTS):
		p += matrix_prices[i][y] * matrix_amounts[i][y]
		q += matrix_prices[i][0] * matrix_amounts[i][y]
	mydict['paasche'] = p/q
	mydict['fisher'] = math.sqrt( mydict['laspeyres'] * mydict['paasche'] )
	matrix_indexes[FIRST_YEAR+y] = mydict

# View.
print 
print "%10.10s" % "Product",
for y in range(FIRST_YEAR,FIRST_YEAR+TOTAL_YEARS):
	print " %16.16s" % y, 
print 
for p in range(PRODUCTS):
	print "%10.10s" % (p+1),
	for y in range(0,TOTAL_YEARS):
		print "%5.0fu x" % matrix_amounts[p][y],
		print "$%7.2f" % matrix_prices[p][y], 
	print 
print 
print "%10.10s %10.10s %10.10s %10.10s %10.10s" % ("Indexes","Simple","Laspeyres","Paasche","Fisher")
for y in range(FIRST_YEAR,FIRST_YEAR+TOTAL_YEARS):
	print "%10.10s %10.4f %10.4f %10.4f %10.4f" % (
		y, matrix_indexes[y]['simple'], matrix_indexes[y]['laspeyres'], matrix_indexes[y]['paasche'], matrix_indexes[y]['fisher'] )
print 

years     = range(FIRST_YEAR,FIRST_YEAR+TOTAL_YEARS)
simple    = [matrix_indexes[x]['simple'] for x in range(FIRST_YEAR,FIRST_YEAR+TOTAL_YEARS)]
laspeyres = [matrix_indexes[x]['laspeyres'] for x in range(FIRST_YEAR,FIRST_YEAR+TOTAL_YEARS)]
paasche   = [matrix_indexes[x]['paasche'] for x in range(FIRST_YEAR,FIRST_YEAR+TOTAL_YEARS)]
fisher    = [matrix_indexes[x]['fisher'] for x in range(FIRST_YEAR,FIRST_YEAR+TOTAL_YEARS)]
plt.plot(years,simple)
plt.plot(years,laspeyres)
plt.plot(years,paasche)
plt.plot(years,fisher)
plt.show()


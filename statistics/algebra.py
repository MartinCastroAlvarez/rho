#!/usr/bin/python
import numpy
import sys

def printArray(title,arr):
	print 
	print title+":"
	for row in arr:
		for col in row:
			print "%-10.2f" % col,
		print ""

A = numpy.array([[1,2,3],[13,4,7],[7,1,5],],dtype=numpy.float32)
B = numpy.array([[6,7,1],[2,3,0],[3,4,4],],dtype=numpy.float32)
printArray("A",A)
printArray("B",B)

print 
print "A.B = sum(A[i]*B[i]) = %i" % numpy.vdot(A,B)
print 
print "det(A) = %i" % numpy.linalg.det(A)
print "The inverse of a matrix will exist only if the determinant is not zero."

printArray("A+B",numpy.add(A,B))
printArray("A-B",numpy.add(A,-B))
printArray("tran(A)",numpy.transpose(A))
printArray("identity(3)",numpy.identity(3))
printArray("AxB = sum(A[n][i]*B[i][n])",numpy.dot(A,B))
printArray("inv(A)",numpy.linalg.inv(A))

def multiplyRow(k,arr):
	if k==0:
		return arr
	m = []
	i = 0 
	while i<len(arr):
		m.append(arr[i]*float(k))
		i+=1
	return m

def sumRows(A,B):
	m = []
	i = 0 
	while i<len(A):
		m.append(float(A[i])-float(B[i]))
		i+=1
	return m

def normaliseRow(arr):
	m=[]
	i=0
	while i<len(arr):
		if arr[i]!=0:
			n = float(arr[i])
			for a in arr:
				m.append(float(a)/float(n))
			return m
		i+=1
	return arr
	
def gauss(A): 
	m = A 
	i = 0
	while i<len(m):
		m[i] = normaliseRow(m[i])
		j=i+1
		while j<len(m):
			a = multiplyRow(m[j][i],m[i])
			b = multiplyRow(m[i][i],m[j])
			c = sumRows(a,b)
			d = normaliseRow(c)
			m[j] = d
			j+=1	
		i+=1
	i-=1
	while i>=0:
		m[i] = normaliseRow(m[i])
		j=i-1
		while j>=0:
			a = multiplyRow(m[j][i],m[i])
			b = multiplyRow(m[i][i],m[j])
			c = sumRows(a,b)
			d = normaliseRow(c)
			m[j] = d
			j-=1
		i-=1
	return m
	 
printArray("Gauss-Jordan",gauss(A))

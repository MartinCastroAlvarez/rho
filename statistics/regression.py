# -*- coding: utf-8 -*-
from __future__ import division
from django.db import models
from django.db import connection
from datetime import datetime, timedelta
from django.db.models import Sum, Avg
from django.contrib.auth.models import User
import heapq
import numpy
import sys
import re

class Regression():

	def __init__(self):
		self.len 	= 0
		self.table 	= []
		self.prediction	= []
		self.z		= []
		self.x		= [] 
		return self

	def getSize(self): return self.len
	def getResults(self): return self.table
	def getPrediction(self): return self.prediction
	def getFormulae(self): return self.z
	def getSample(self): return self.x
	def predict(self): pass

	def __unicode__(self):
		i = 0 
		str = "\n %-5s %-13s %-13s \n" % ( "", "Sample", "Regression" ) 
		while i < len(self.table):
			str += " %-5d %-13.2f %-13.2f\n" % ( i, self.x[i], self.table[i] )
			i = i + 1
		m = 0
		str += "\n %-5s %-13s %-13s \n" % ( "", "", "Prediction" ) 
		while m < len(self.prediction):
			str += " %-5d %-13s %-13.2f\n" % ( i, "", self.prediction[m] )
			i = i + 1
			m = m + 1
		return str

class LinearRegression(Regression):

	def __init__(self,array,predict=5): 
		Regression.__init__(self)
		x = []
		y = []
		i = 0 
		for a in array:
			x.append(a)
			y.append(i)	
			i = i + 1

		self.x = numpy.array(x)
		self.y = numpy.array(y)
		self.len = len(self.x)
		self.A = numpy.vstack([self.x, numpy.ones(len(self.x))]).T
		self.m, self.c = numpy.linalg.lstsq(self.A, self.y)[0]
		self.z = [self.m, self.c]

		self.cycle_error	= []
		self.cycle_trend	= []
		i = 0 
		while i < len(array):

			value = self.predict(i)
			self.table.append(value)

			if value and array[i]:
				error = array[i] / value
			else:
				error = 0
			self.cycle_error.append(error)

			if i == 0:
				self.cycle_trend.append(" ")
			elif self.cycle_error[i] > self.cycle_error[i-1]:
				self.cycle_trend.append("+")
			else:
				self.cycle_trend.append("-")

			i = i + 1 

		while i < len(array) + predict:
			self.prediction.append( self.predict(i) )
			i = i + 1 

	def getCycleError(self): return self.cycle_error
	def getCycleTrend(self): return self.cycle_trend
	def predict(self,x): return x * self.m + self.c

class PolyRegression(Regression):

	def __init__(self,array,degree=3,predict=5): 
		Regression.__init__(self)
		self.degree = degree
		x = []
		y = []
		i = 0 
		for a in array:
			x.append(a)
			y.append(i)	
			i = i + 1

		self.x = numpy.array(x)
		self.y = numpy.array(y)
		self.l = len(self.x)
		self.z = numpy.polyfit(self.x, self.y, degree)
		self.p = numpy.poly1d(self.z)
		i = 0 
		while i < self.l:
			self.table.append( self.predict(i) )
			i = i + 1
		while i < self.l + predict:
			self.prediction.append( self.predict(i) )
			i = i + 1

	def predict(self,x):	
		n = 0 
		r = 0
		while n <= self.degree:
			c = self.p[n]
			r += c * (x ** n)
			print(" %.2f = %.2f * %d  %d " % (r,c,x,n))
			n = n + 1
		return r

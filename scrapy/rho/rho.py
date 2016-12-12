#!/usr/bin/python
from openpyxl.styles import Style, Font, Alignment
from lxml import etree
import cookielib
import requests
import openpyxl
import time
import sys

class RhoHTTP:

	PURPLE          = '\033[95m'
	CYAN            = '\033[96m'
	DARKCYAN        = '\033[36m'
	BLUE            = '\033[94m'
	GREEN           = '\033[92m'
	YELLOW          = '\033[93m'
	RED             = '\033[91m'
	BOLD 		= '\033[1m'
	UNDERLINE       = '\033[4m'
	END             = '\033[0m'

	def __init__(self):
		self.session	= requests.Session()
		self.jar	=  cookielib.CookieJar()
		self.parser 	= etree.HTMLParser()

	def http(self,url,data=None,debug=False):
		if data:	
			print "POST "+url
			r = self.session.post(url,data=data,verify=False,cookies=self.jar)
		else:
			print "GET "+url
			r = self.session.get(url,verify=False,cookies=self.jar)
		if debug:
			FILENAME = "/tmp/HTTP.%i.html" % time.time()
			text_file = open(FILENAME, "w")
			text_file.write(r.text.encode("utf-8","ignore")) 
			text_file.close()	
			print self.RED + FILENAME + self.END 
		if r.status_code != 200:
			raise Exception("URL RETURNED STATUS %s" % r.status_code)	
		return r.text.encode("utf-8","ignore")

	def debugXML(self,elem):
		print(etree.tostring(elem, pretty_print=True))	

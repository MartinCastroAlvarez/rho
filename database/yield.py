import json
import sys
import cookielib
import requests
import fileinput
import subprocess
from geopy.distance import vincenty
import time

class BerlinConnection:

	def __init__(self,url):
		print("Someday this database may evolve into SQL...")
		self.root = url
		self.jar = cookielib.CookieJar()
		self.web = requests.Session()

	def get(self,path):
		url = "%s/%s" % (self.root,path)
		print("GET %s" % url)
		r =  self.web.get(url,verify=False,cookies=self.jar)
		data = json.loads(r.text)
		return data

	def close(self):
		self.web.close()

class BerlinDatabase:

	def __init__(self,name):
		self.name = "/tmp/%s-%f" % (name,time.time())
		self.clean()

	def clean(self):
		file = open(self.name,"w")
		file.close()

	def save(self,data):
		file = open(self.name,"a")
		for d in data: 
			j = json.dumps(d)
			file.write(j)
			file.write("\n")
		file.close()

	def read(self):
		file = open(self.name) 
		for line in file:
			yield json.loads(line)
		file.close()

	def isEmpty(self):
		return self.count()<1

	def count(self):
		return sum(1 for line in open(self.name))

	def close(self):
		""" Not implemented """
		pass 

class Resmio:
	
	def __init__(self,lat,lng,kms):
		assert kms>0, "Distance must be a positive number"
		self.position = (lng,lat)
		self.cache = [] 
		self.distance = kms * 1000
		self.web = BerlinConnection('https://api.resmio.com/v1')
		self.db = BerlinDatabase("resmio-db")
		self.cache = BerlinDatabase("resmio-cache")

	def close(self):
		self.web.close()
		self.db.close()

	def getDatabase(self):
		return self.db

	def loadNearFascilities(self):
		self.cache.clean()
		more_exist = True
		offset = 0 
		limit = 30
		while more_exist: 
			params = "&".join([
				"near=%f,%f" % self.position,
				"distance=%i" % self.distance,
				"limit=%i" % limit,
				"offset=%i" % offset,
			]) 
			data =  self.web.get('facility?%s'%params)
			results = []
			for d in data['objects']:
				results.append(d)
			self.db.save(results)
			more_exist = data['meta']['next'] is not None
			offset += limit

	def getClosests(self):
		if self.cache.isEmpty:
			results = []
			for restaurant in r.db.read():
				id = restaurant['id'] 
				distance = vincenty(self.position, restaurant['location']).meters
				results.append({
					'id': 		id, 
					'distance':  	distance,
				})
			i = 0 
			while i<len(results):
				j = i+1
				while j<len(results):
					if results[i]['distance'] > results[j]['distance']: 
						results[i], results[j] = results[j], results[i]
					j += 1 
				i += 1 
			self.cache.save(results)
		return self.cache.read()

	def getDensity(self):
		restaurants = self.db.count()	
		kilometers = self.distance / 1000
		total = restaurants / kilometers
		return total


lat = 52.516667
lng = 13.383333
kms = 5
print("Starting application at lat=%f lng=%f with a distance of %ikm(s)..." %(lat,lng,kms))
r = Resmio(lat=lat,lng=lng,kms=kms)

print("\n1) Querying API for all restaurants around the center of Berlin...")
r.loadNearFascilities()

print("\n2) Finding the 5 closests restaurants' centroid...")
gen = r.getClosests()
for i in range(0,5):
	try: 
		x = gen.next()
		print("%-25.25s"% x['id'])
	except:
		break 

print("\n3) Calculating the density of the restaurants per square kilometre at the centroid...")
print("%-12.12s %10.0i R"	% ("Restaurants:",r.getDatabase().count()))
print("%-12.12s %10.0i kms"	% ("Kilometers:",kms))
print("%-12.12s %10.2f R/km2"	% ("Density:",r.getDensity()))

print("\n4) Calculating the distances of the five closests restaurants to the centroid...")
gen = r.getClosests()
for i in range(0,5):
	try: 
		x = gen.next()
		print("%-25.25s %10.2f mts"% (x['id'],x['distance']) )
	except:
		break 

print "..."

print("\nClosing connections...")
r.close()

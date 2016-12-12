""" Proxy pattern applied to Python by martincastro.10.5@gmail.com """
class Datasource:
	
	def __init__(self,ip):
		self.ip = ip
		print "Conneting to %s with a low connetion..." % self.ip
	
	def __str__(self):
		return "Datasource: %s" % self.ip

class DatasourceProxy(Datasource):

	ds = {}
	
	def __init__(self,ip):
		if ip not in self.__class__.ds:
			self.__class__.ds[ip] = Datasource(ip)
		self.mydb = self.__class__.ds[ip]

	def __str__(self):
		return self.mydb.__str__()

print "Slow connection without proxy:"
ds1 = Datasource('120.12.23.1')
ds2 = Datasource('120.12.23.1')
ds3 = Datasource('120.12.23.1')
print ds1, ds2, ds3

print "Fast connection using proxy:"
ds1 = DatasourceProxy('120.12.23.1')
ds2 = DatasourceProxy('120.12.23.1')
ds3 = DatasourceProxy('120.12.23.1')
print ds1, ds2, ds3

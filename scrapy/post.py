import cookielib
import requests

jar = cookielib.CookieJar()
url = "http://www.google.com"
web = requests.Session()
r1  = web.get(url,cookies=jar,verify=False)
print r1.text
data = dict(a=1,b=2,c=3)
r2 = web.post(url,cookies=jar,data=data)
print r2

import urllib
import urllib2
import json

request_headers = {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token 1dcf26a7307f01b81955cc135df2790a61527f91'
}

url='https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'

req=urllib2.Request(url,headers=request_headers)
res=urllib2.urlopen(req)

data=res.read()
f= open('/tmp/37','w')
f.write(data)
print 'The file was saved!'

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

data= json.loads(res.read())['items']

owners={}
ownerlocations=[]

for item in data:
    owners[item['owner']['login']]=item['full_name']

for owner in owners:
    url='https://api.github.com/users/'+owner
    req=urllib2.Request(url,headers=request_headers)
    res=urllib2.urlopen(req)
    location= json.loads(res.read())['location']
    #ownerlocations[owner]=Repo(owners[owner],location)
    ownerlocations.append({'location':location, 'full_name':owners[owner]})

print json.dumps(ownerlocations,sort_keys=True)
          




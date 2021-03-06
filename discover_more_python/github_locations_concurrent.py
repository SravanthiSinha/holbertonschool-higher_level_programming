import urllib
import urllib2
import json
import Queue
import threading

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
threads=[]
for item in data:
    owners[item['owner']['login']]=item['full_name']

def get_location(owner):
    url='https://api.github.com/users/'+owner
    req=urllib2.Request(url,headers=request_headers)
    res=urllib2.urlopen(req)
    location= json.loads(res.read())['location']
    ownerlocations.append({'location':location, 'full_name':owners[owner]})
    
for owner in owners:
    threads.append(threading.Thread(target=get_location,args=[owner]))

for x in threads:
    x.start();

    
for thread in threads:
    thread.join()

print json.dumps(ownerlocations,sort_keys=True)
          




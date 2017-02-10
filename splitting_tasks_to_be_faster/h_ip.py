from threading import Thread,Lock,active_count
from urllib2 import urlopen
import json

class IPThread(Thread):

    def __init__(self, ip, callback):
        self.ip = ip
        self.callback = callback
        Thread.__init__(self)

    def run(self):
        print "Search: {}".format(self.ip)
        page = urlopen ("https://api.ip2country.info/ip?"+self.ip)
        json_str = json.loads(page.read())
        self.callback(json_str['countryName'])
        print "countryName: {}".format(json_str['countryName'])



from threading import Thread,Lock,active_count
from urllib2 import urlopen


class LoripsumThread(Thread):

    def __init__(self, filename):
        self.filename = filename
        Thread.__init__(self)

    def run(self):
        with Lock():
            page = urlopen ("http://loripsum.net/api/1/short ")
            with open(self.filename, "a") as f:
                f.write(page.read())



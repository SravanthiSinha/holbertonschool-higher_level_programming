from threading import BoundedSemaphore
from random import randint
from time import sleep

class Store:

    nbpersoninside = 0
    semaphore = None
    
    def __init__(self, item_number, person_capacity):
        global nbpersoninside,s,pool        
        self.item_number = item_number
        self.person_capacity = person_capacity
        self.semaphore = BoundedSemaphore(self.person_capacity)

    def enter(self):
        if self.nbpersoninside < self.person_capacity:
            self.nbpersoninside += 1
        self.semaphore.acquire()

            

    def buy(self):
        sleep(randint(5,10))
        if self.item_number > 0:
            self.item_number -= 1
            self.nbpersoninside -= 1
            self.semaphore.release()
            return True
        else:
            self.nbpersoninside -= 1
            self.semaphore.release()
            return False
            
        

import threading

class OrderedArray():
    list = []

    def  __init__(self):
        self.__threads = []
    
    def add(self, number):
        if not isinstance(number,int):
            raise Exception("number is not an integer")
        order_thread = OrderedArrayThread(number)
        self.__threads += [order_thread]
        order_thread.start()

    def isSorting(self):
        for t in self.__threads:
            if t.isAlive():
                return True
        return False

    def __str__(self):
        return str(OrderedArray.list)

    
class OrderedArrayThread(threading.Thread):
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        if not isinstance(number,int):
            raise Exception("number is not an integer")
        self.__number = number
    
    def run(self):
        OrderedArrayThread.lock.acquire()
        OrderedArray.list += [self.__number]
        OrderedArray.list.sort()
        OrderedArrayThread.lock.release()
    

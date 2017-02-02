import threading

lock = threading.Lock()

class Sum():
    total = 0
    def __init__(self, nb_threads, numbers):
        Sum.total = 0
        if not isinstance(nb_threads,int):
            raise Exception("nb_threads is not an integer")
        if not all(isinstance(number,int) for number in numbers):
            raise Exception("numbers is not an array of integers")
        self.__threads = []
        self.__nb_threads = nb_threads
        chunk = int(len(numbers)/nb_threads)
        for i in range(nb_threads-1):
            sumthread = SumThread(numbers[chunk*i:chunk*(i+1)])
            self.__threads += [sumthread]
            sumthread.start()
        sumthread = SumThread(numbers[chunk*(nb_threads-1):])
        self.__threads += [sumthread]
        sumthread.start()
        
    def isComputing(self):
       for t in self.__threads:
           if t.isAlive():
               return True
       return False

    def __str__(self):
        with lock:
            return str(Sum.total)

    
class SumThread(threading.Thread):

    def __init__(self, numbers):
        threading.Thread.__init__(self)
        if not all(isinstance(number,int) for number in numbers):
            raise Exception("numbers is not an array of integers")
        self.__numbers = numbers
    
    def run(self):
        lock.acquire()
        Sum.total += sum(self.__numbers)
        lock.release()
    

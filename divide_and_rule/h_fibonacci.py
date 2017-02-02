import threading

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


class FibonacciThread(threading.Thread):

    def __init__(self, number):
        threading.Thread.__init__(self)
        if not isinstance(number,int):
            raise Exception("number is not an integer")
        self.__number = number

        
    def run(self):
        print "%d => %d" %(self.__number, fib(self.__number))
        
    

import threading

class ReverseStrThread(threading.Thread):
    
    sentence = ""
    
    def __init__(self, word):
        threading.Thread.__init__(self)
        if not isinstance(word, str):
            raise Exception("word is not a string")
        else:
            
            self.__word = word
    
    def run(self):
        ReverseStrThread.sentence += " "+self.__word[::-1]

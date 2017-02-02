import threading
import sys

class StrLenThread(threading.Thread):

    def __init__(self, word):
        threading.Thread.__init__(self)
        if not isinstance(word,str):
            raise Exception("word is not a string")
        self.__word = word

        
    def run(self):
        global total_str_length
        total_str_length +=len(self.__word)
        
    
text = sys.argv[1]

words = text.split(" ")
str_len_threads = []

total_str_length = len(words) - 1
    
for word in words:
    str_len_thread = StrLenThread(word)
    str_len_threads += [str_len_thread]
    str_len_thread.start()
    
for t in str_len_threads:
    t.join()

print "%d"  % total_str_length

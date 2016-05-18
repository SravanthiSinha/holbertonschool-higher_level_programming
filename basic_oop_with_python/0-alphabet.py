import sys

''' print the alphabets '''
def print_alphabets():
    for i in range(97,97+26):
        sys.stdout.write(chr(i))
    print 
    
print_alphabets()

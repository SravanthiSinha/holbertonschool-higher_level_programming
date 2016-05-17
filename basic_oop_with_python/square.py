import math
import sys

'''Class Square'''
class Square():

    ''' Constructor '''
    def __init__(self, side_length):
        self.__side_length = side_length
        self.name = ''
        
    def __str__(self):
        self.__printline('*','*',self.__side_length)
        
    def __printline(self,c,m,n):
        if c == m :
            for i in range(1,n):
                sys.stdout.write(c)    
        else:
            sys.std.write(c)
            for i in range(1,n-2):
                sys.stdout.write(m)    
            sys.stdout.write(m)
                
    '''   Getter for color '''
    def get_color(self):
        return self.__color

    ''' Setter for color '''
    def set_color(self, color):
        self.__color = color;

    ''' Getter for center'''
    def get_center(self):
        return self.__center

    ''' Setter for center'''
    def set_center(self, center):
        self.__center = center

        
    ''' calculate and return the area of the circle'''
    def area(self):
        return self.__side_length**2


        

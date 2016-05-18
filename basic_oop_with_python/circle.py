import math
'''Class Circle'''
class Circle():

    ''' Constructor '''
    def __init__(self, radius):
        self.__radius = radius
        self.name = ''
        
    ''' Getter for color '''
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
        return math.pi*self.__radius**2


        
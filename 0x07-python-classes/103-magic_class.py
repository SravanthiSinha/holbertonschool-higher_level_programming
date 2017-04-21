#!/usr/bin/python3
import math
"""MagicClass: basic bytecode for a class declaration"""


class MagicClass:
    """ doesn't do much """
    def __init__(self, radius=0):
        """init"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ return area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ return circumference """
        return 2 * math.pi * self.__radius

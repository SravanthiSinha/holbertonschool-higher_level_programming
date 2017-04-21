#!/usr/bin/python3
"""
This is the Square module.
This module provides a simple Square class with initialize size.
Defaults size to 0. Raise error on invalid size inputs.
Methods Getter and Setter properties for size.
Method area returns size of area of the square.
"""


class Square:
    """
    This is a Square class
    """
    def __init__(self, size=0):
        """
        Initializes the square and the size
        """
        self.size = size

    @property
    def size(self):
        """
        returns the size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets the size of square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """
        returns the current square area
        """
        return (self.__size * self.__size)

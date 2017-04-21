#!/usr/bin/python3
"""
This is the Square module.
This is a Square class inside the square module.
"""


class Square:
    """
    This is a Square class
    """
    def __init__(self, size=0):
        """
        Initializes the square and the __size
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

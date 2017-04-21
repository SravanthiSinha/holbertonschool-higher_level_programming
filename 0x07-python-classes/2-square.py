#!/usr/bin/python3
"""
This is the Square module.
This is a Square class inside the square module.
"""


class Square:
    """
    This is a square class
    """
    def __init__(self, size = 0):
        """
        Initializes the square and the __size
        """
        if type(size) is not int:
                raise TypeError("size must be an integer")
        elif size < 0:
                raise ValueError("size must be >= 0")
        self.__size = size

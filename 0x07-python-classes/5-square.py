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
        Initializes the square and the size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """
        returns the current square area
        """
        return (self.__size * self.__size)


    def my_print(self):
        """
        prints the # size times
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * "#")

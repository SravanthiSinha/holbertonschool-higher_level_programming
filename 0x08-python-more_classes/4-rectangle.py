#!/usr/bin/python3
"""
This is the Rectangle module.
This is a Rectangle class inside the Rectangle module.
"""


class Rectangle:
    """
    This is a Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle and the __width
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if width < 0:
                raise ValueError('height must be >= 0')
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if(self.__height == 0 or self.__width == 0):
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        if(self.__height == 0 or self.__width == 0):
            return ""
        string = (('#' * self.__width) + '\n') * self.__height
        return string[:-1]

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

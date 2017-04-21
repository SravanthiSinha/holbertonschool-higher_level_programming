#!/usr/bin/python3
"""
Square class with basic printing function
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize square with size and pos
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        errormsg = 'position must be a tuple of 2 positive integers'
        if type(position) is not tuple:
            raise TypeError(errormsg)
        if len(position) != 2:
            raise TypeError(errormsg)
        for i in position:
            if type(i) is not int or i < 0:
                raise TypeError(errormsg)
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        errormsg = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple:
            raise TypeError(errormsg)
        if len(value) != 2:
            raise TypeError(errormsg)
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError(errormsg)
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.__size
                             for i in range(self.__size)]))

    def __str__(self):
        """ does this need this """
        if self.__size == 0:
            return("")
        return(("\n" * self.__position[1]) +
               ("\n".join((" " * self.__position[0]) +
                          "#" * self.__size for i in range(self.__size))))

# Python - Classes and Objects

# Square Class - its methods and attributes.

* Private instance attribute: size:
..* property def size(self): to retrieve it
..* property setter def size(self, value): to set it:
                *size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
                *if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Private instance attribute: position:
..* property def position(self): to retrieve it
..* property setter def position(self, value): to set it:
                *position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
..* if size is equal to 0, print an empty line
..* position should be use by using space
* Printing a Square instance should have the same behavior as my_print()


# Useful links for PEP8 style and doctest:
https://pypi.python.org/pypi/pep8
https://pymotw.com/2/doctest/
https://docs.python.org/3.4/library/doctest.html

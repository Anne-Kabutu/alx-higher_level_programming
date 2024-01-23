#!/usr/bin/python3
"""
Module: Square class
"""


class Square:
    """
    Class Square that defines square object
    """
    def __init__(self, size=0):
        """
        Initialisation of the object with size set to default 0

        Args:
            size: size of the side of the square

        Attributes:
            __size: size of the side of the square set privately
                    defaults to 0 if None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

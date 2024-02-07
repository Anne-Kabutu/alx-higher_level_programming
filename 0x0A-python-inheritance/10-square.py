#!/usr/bin/python3
"""
Module: 10-square

Contains parent class BaseGeometry
with public instance method area and integer_validation

Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__

Contains subclass Square
with instantiation of private attribute size, validated by superclass
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle, who inherits from BaseGeometry
    """
    def __init__(self, size):
        """
        initialize size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

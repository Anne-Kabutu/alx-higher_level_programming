#!/usr/bin/python3
""" Module: 8-rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits BaseGeometry class
    """
    def __init__(self, width, height):
        """
        Initialising function of width and height of rectangle
        Validates the values before assigning
        It privately stores the values validated
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

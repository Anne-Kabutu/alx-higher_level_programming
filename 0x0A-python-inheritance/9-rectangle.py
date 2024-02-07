#!/usr/bin/python3
""" Module: 9-rectangle """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class that defines rectangle from Base Geometry Class
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

    def area(self):
        """ Method that returns area of the instance """
        return self.__width * self.__height

    def __str__(self):
        """ Returns string representation """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

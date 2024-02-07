#!/usr/bin/python3
""" Module: 7-base_geometry """


class BaseGeometry():
    """
    Base Geometry class with the function of area
    """
    def area(self):
        """
        Public instance method that raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance that validates the input
        Args:
            name (str): assumed as always string
            value (int): greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

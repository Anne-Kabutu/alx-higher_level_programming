#!/usr/bin/python3
""" Module: 3-is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """
    Function that checks if the obj passed as parameter
    is an instance of the class passed as param too

    obj: param of the object to check

    a_class: the class to check if object inherits

    Returns: True is true otherwise False
    """
    return isinstance(obj, a_class)

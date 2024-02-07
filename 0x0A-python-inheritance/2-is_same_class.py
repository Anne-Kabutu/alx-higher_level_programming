#!/usr/bin/python3
""" Module: 2-is_same_class """


def is_same_class(obj, a_class):
    """
    Function that checks if the obj passed as parameter
    is same as the class passed as param too

    obj: param of the object to check

    a_class: the class to check if object is same

    Returns: True is true otherwise False
    """
    return type(obj) is a_class

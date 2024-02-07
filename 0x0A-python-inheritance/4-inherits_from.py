#!/usr/bin/python3
""" Module: 4-inherits_from.py """


def inherits_from(obj, a_class):
    """
    Function that checks if object passed is
    a direct instance of the class
    or indirectly inherits from the class
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))

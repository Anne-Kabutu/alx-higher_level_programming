#!/usr/bin/python3
""" Module: 101-add_attribute """


def add_attribute(obj, name, value):
    """
    Function that adds a new attribute to an object

    Args:
        obj: object
        name: attribute name
        value: value of attribute
    Raises TypeError if attribute cant be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)

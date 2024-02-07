#!/usr/bin/python3
""" Module: 8-class_to_json """


"""
returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """
    return obj.__dict__

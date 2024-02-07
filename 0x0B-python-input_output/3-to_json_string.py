#!/usr/bin/python3
""" Module: 3-to_json_string """


import json


def to_json_string(my_obj):
    """
    Function that returns json representation of an object
    (string)
    """
    return json.dumps(my_obj)

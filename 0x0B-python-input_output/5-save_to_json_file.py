#!/usr/bin/python3
""" Module: 5-save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes python obj to file using json rep
    Args:
        my_obj: python obj
        filename: file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)#!/usr/bin/python3
""" Module: 5-save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes python obj to file using json rep
    Args:
        my_obj: python obj
        filename: file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """
    function that prints an integer
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as i:
        stderr.write("Exception: {}\n".format(i))
        return (False)

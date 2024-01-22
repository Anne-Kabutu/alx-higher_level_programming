#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides 2 integers and prints result
    """
    try:
        result = (a / b)
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)

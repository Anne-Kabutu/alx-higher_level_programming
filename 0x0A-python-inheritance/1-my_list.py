#!/usr/bin/python3
""" Module: my_list """


class MyList(list):
    """
    Class that inherits the attributes and methods of
    class list
    """
    def print_sorted(self):
        """ Method that prints a sorted list """
        print(sorted(self))

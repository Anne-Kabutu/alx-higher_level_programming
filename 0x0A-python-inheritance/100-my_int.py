#!/usr/bin/python3
""" Module: 100-my_int """


class MyInt(int):
    """
    MyInt inherits int class
    """

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)

#!/usr/bin/python3
""" Module: 2-append_write """


def append_write(filename="", text=""):
    """
    Function that appends a string at the end
    of text file
    Returns no of characters written/added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

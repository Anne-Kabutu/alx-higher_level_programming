#!/usr/bin/python3
""" Module: 1-write_file """


def write_file(filename="", text=""):
    """
    Function that writes a string to text file
    Returns number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))

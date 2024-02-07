#!/usr/bin/python3
""" Module: 0-read_file """


def read_file(filename=""):
    """ function that opens file, read and prints data """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end="")

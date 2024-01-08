#!/usr/bin/python3
def no_c(my_string):
    copy = my_string[:]
    return ("".join(char for char in copy if char not in "cC"))

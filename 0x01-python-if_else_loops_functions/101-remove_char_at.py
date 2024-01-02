#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for char in range(0, len(str)):
        if char != n:
            copy = copy + str[char]
    return copy

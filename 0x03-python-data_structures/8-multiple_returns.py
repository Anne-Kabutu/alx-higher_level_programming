#!/usr/bin/python3
def multiple_returns(sentence):
    nums = len(sentence)
    if nums == 0:
        f_char = None
    else:
        f_char = sentence[0]
    t = (nums, f_char)
    return t

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    part_1a = tuple_a[0] if len_a > 0 else 0
    part_1b = tuple_b[0] if len_b > 0 else 0
    part_2a = tuple_a[1] if len_a > 1 else 0
    part_2b = tuple_b[1] if len_b > 1 else 0

    sum = (part_1a + part_1b), (part_2a + part_2b)

    return sum

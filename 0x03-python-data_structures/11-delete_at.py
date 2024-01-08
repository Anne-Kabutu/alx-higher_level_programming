#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    nums = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= nums:
        return my_list
    else:
        del my_list[idx]
        return my_list

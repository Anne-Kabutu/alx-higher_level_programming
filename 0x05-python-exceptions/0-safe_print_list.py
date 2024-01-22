#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    function to print no of elements without len()
    """
    count = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end="")
        except IndexError:
            break
        else:
            count += 1
    print()
    return (count)

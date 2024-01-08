#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    function to print a matrix
    """
    for i in matrix:
        for j in range(len(i)):
            print("{:d}".format(i[j]), end="" if j == (len(i) - 1) else " ")
            # if j == (len(i) - 1):
            #     print("{:d}".format(i[j]), end="")
            # else:
            #     print("{:d} ".format(i[j]), end="")
        print()

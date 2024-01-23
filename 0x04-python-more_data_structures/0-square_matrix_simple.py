#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # computes the square of all ints of a matrix
    if matrix is not None:
        square = []
        for i in matrix:
            square.append(list(map(lambda x: x * x, i)))
    return square


'''
if len(matrix) != 0:
    copy = matrix[:]
        squares = []
    for i in matrix:
        copy = list(map(lambda x: x * x, i))
        squares.append(copy)
    return squares
'''

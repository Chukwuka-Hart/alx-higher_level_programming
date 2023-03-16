#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for elems in matrix:
        new_matrix.append(list(map(lambda x: x * x, elems)))

    return new_matrix

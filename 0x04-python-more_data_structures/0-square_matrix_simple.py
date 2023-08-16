#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for ls in range(len(matrix)):
        new_matrix[ls] = list(map(lambda value: value**2, matrix[ls]))

    return new_matrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        inner = []
        for j in range(len(matrix[i])):
            squares = (matrix[i][j] ** 2)
            inner.append(squares)
        result.append(inner)
    return result

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    z = []
    zz = []
    for i in matrix:
        for j in i:
            z.append(j * j)
        zz.append(z)
        z = []
    return (zz)

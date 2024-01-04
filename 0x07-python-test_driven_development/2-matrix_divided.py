#!/usr/bin/python3
def matrix_divided(matrix, div):
    y0 = 0
    y1 = 0
    m = []
    mm = []
    for i in matrix:
        for j in i:
            y0 = j / div
            y1 = round(y0, 2)
            mm.append(y1)
        m.append(mm)
        mm = []
    return m

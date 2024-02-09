#!/usr/bin/python3
def matrix_divided(matrix, div):
    y0 = 0
    y1 = 0
    m = []
    mm = []
    if type(div) != int and type(div) != float:
        raise ValueError("a must be an integer")
    for i in matrix:
        if type(i) != int and type(i) != float:
                raise ValueError("a must be an integer")
        for j in i:
            if type(j) != int and type(j) != float:
                raise ValueError("a must be an integer")
            y0 = j / div
            y1 = round(y0, 2)
            mm.append(y1)
        m.append(mm)
        mm = []
    return m
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

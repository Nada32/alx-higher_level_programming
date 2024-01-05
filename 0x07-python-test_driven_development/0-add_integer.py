#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) != int and type(a) != float:
        raise ValueError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise ValueError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return (a + b)

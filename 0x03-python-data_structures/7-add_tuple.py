#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    z = []
    x = 0
    y = 0
    if len(tuple_b) < len(tuple_a):
        x = len(tuple_b)
        y = len(tuple_a)
    elif len(tuple_a) < len(tuple_b):
        x = len(tuple_a)
        y = len(tuple_b)
    #for i in range(y):
    for j in range(x):
        z.append(tuple_a[j] + tuple_b[j])
    for j in range(y - x):
        if len(tuple_b) < len(tuple_a):
            z.append(tuple_a[y - x + j])
        elif len(tuple_a) < len(tuple_b):
            z.append(tuple_b[y - x + j])
    print("(", end="")
    for i in range(len(z)):
        print("{}".format(z[i]), end="")
        if i < len(z) - 1:
            print(", ", end="")
    print(")")

#!/usr/bin/python3
for i in range(99):
    x = "{:02}".format(i)
    if x[0] < x[1]:
        if x != '89':
            print("{}".format(x), end=", ")
print("89")

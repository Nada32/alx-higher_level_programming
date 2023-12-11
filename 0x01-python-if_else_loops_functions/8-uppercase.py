#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if i > chr(96) and i < chr(97+26):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()

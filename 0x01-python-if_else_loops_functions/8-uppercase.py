#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if i > chr(96) and i < chr(97+26):
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print("{}".format(i), end='')

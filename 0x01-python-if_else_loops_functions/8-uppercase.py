#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if i > chr(96) and i < chr(97+26):
            print(chr(ord(i) - 32), end='')
        else:
            print(i, end='')

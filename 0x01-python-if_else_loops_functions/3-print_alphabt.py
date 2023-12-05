#!/usr/bin/python3
for i in range(26):
    if chr(i + 97) != 'e' and chr(i + 97) != 'q':
        print("{}".format(chr(i + 97)), end="")

#!/usr/bin/python3
import sys
n = len(sys.argv)
print("{} arguments".format(n))
for i in range(1, n):
    if n > 0:
        print("{:d} : {}".format(i, sys.argv[i]))
    elif n == 0:
        print(".")

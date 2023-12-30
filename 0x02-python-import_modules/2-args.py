#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n == 2:
        print("{} argument:".format(n - 1), end="")
    elif n > 1:
        print("{} arguments:".format(n - 1), end="")
    elif n == 1:
        print("{} arguments.".format(n - 1), end="")
    if n > 0:
        print("\n", end="")
    for i in range(1, n):
        if n > 0:
            print("{:d}: {}".format(i, argv[i]))

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    print("{} arguments".format(n))
    for i in range(1, n):
        if n > 0:
            print("{:d} : {}".format(i, argv[i]))
        elif n == 0:
            print(".")

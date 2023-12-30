#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    z = 0
    for i in range(1, n):
        if argv[i] == '-':
            d = -1 * int(argv[i + 1])
            i = i + 1
        else:
            d = int(argv[i])
        z = z + d
    print("{:d}".format(z))

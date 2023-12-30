#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    z = 0
    for i in range(1, n):
        if i == '-':
            d = -1 * int(i + 1)
            i++
        else:
            d = int(i)
        z = z + d
    print("{:d}".format(z))

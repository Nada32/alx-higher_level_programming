#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    print("{} argument:".format(n - 1), end="")
    if n > 0:
        print("\n", end="")
    elif n == 0:
        print(".")
    for i in range(1, n):
        if n > 0:
            print("{:d}: {}".format(i, argv[i]))

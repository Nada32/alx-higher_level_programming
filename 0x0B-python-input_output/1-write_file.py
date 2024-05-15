#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ method """
    z = 0
    with open(filename, 'w', encoding="utf-8") as f:
        for line in f:
            z = z + 1
    return (z)

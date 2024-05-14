#!/usr/bin/python3
""" module """


def read_file(filename=""):
    """ method """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")

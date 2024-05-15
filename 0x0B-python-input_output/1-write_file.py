#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ method """
    with open(filename, 'w', encoding="utf-8") as f:
        return len(f.write(text))

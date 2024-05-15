#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ method """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))

#!/usr/bin/python3
""" module """


def append_write(filename="", text=""):
    """ method """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))

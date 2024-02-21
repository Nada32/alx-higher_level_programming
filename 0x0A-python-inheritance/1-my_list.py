#!/usr/bin/python3
"""
contains the MyList class
"""


class Mylist(list):
    """Empty class"""
    pass

    def print_sorted(self):
        """meth"""
        print(sorted(list(self)))

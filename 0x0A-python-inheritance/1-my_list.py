#!/usr/bin/python3
"""
contains the MyList class
"""


class Mylist(list):
    """ Class inherits from list"""
    pass

    def print_sorted(self):
        """Method prints the list, but sorted"""
        print(sorted(list(self)))

#!/usr/bin/python3
"""
contains the MyList class
"""


class Mylist(list):
    """ This class inherits from list() """

    def print_sorted(self):
        """ Print a list in sorted ascending order. """
        print(sorted(self))

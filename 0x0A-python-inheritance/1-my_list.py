#!/usr/bin/python3
"""
contains the MyList class
"""


class Mylist(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))

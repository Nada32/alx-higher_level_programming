#!/usr/bin/python3
"""class module"""


class Square():
    """Empty class"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self, area):
        return (self.__size * self.__size)

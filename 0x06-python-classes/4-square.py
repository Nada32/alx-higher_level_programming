#!/usr/bin/python3
class Square():
    """Empty class"""
    def __init__(self, size=0):
        self.__size = size

    def size(self):

        return (self.__size)
    def size(self, value):

        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    def area(self):

        return (self.__size * self.__size)

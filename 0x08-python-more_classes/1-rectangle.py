#!/usr/bin/python3
"""class module"""


class Rectangle():
    """Empty class"""
    def __init__(self, size=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):

        return (self.__width)

    @width.setter
    def width(self, value):

        self.__size = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):

        return (self.__height)

    @height.setter
    def height(self, value):

        self.__size = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
    def area(self):

        return (self.__width * self.__height)

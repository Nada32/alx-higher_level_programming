#!/usr/bin/python3
""" module """

class Student():
    """ hi s """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def to_json(self):
        """ hi """
        return (self.__dict__)

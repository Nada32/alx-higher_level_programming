#!/usr/bin/python3
""" module """

import json


def save_to_json_file(my_obj, filename):
    """ method """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

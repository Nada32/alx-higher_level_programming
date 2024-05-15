#!/usr/bin/python3
""" module """

import json


def load_from_json_file(filename):
    """ method """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f))

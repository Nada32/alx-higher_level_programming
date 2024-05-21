#!/usr/bin/python3
"""module"""
import json
import sys





if __name__ == "__main__":
    """hi"""
    from 5-save_to_json_file import save_to_json_file
    from 6-load_from_json_file.py import load_from_json_file
    from sys import argv


    filename = "add_item.json"
    jsonlist = []

    if os.path.exists(filename):
        json_list = load_from_json_file(filename)

    for index in argv[1:]:
        json_list.append(index)

    save_to_json_file(json_list, filename)

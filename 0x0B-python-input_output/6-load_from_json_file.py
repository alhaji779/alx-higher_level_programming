#!/usr/bin/python3
""" Convert  json file to python object """


def load_from_json_file(filename):
    """ function to get python obj from json file 
    """
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


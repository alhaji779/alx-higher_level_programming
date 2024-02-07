#!/usr/bin/python3
""" convert json string back to python object """


def from_json_string(my_str):
    """ function to convert json str to python object """
    import json

    return json.load(my_str)

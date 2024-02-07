#!/usr/bin/python3
""" converting objs to string """


def to_json_string(my_obj):
    """ function to convert obj to string """
    import json

    return json.dumps(my_obj)

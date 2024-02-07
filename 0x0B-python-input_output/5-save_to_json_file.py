#!/usr/bin/python3
""" save obj file in json format """


def save_to_json_file(my_obj, filename):
    """ save file as json string """
    import json

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))

#!/usr/bin/python3
""" add items from screen into python list """


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

from sys import argv

try:
    lst = load_file('add_item.json')
except:
    lst = []

for i in argv[1:]:
    lst.append(i)

save_file(lst, 'add_item.json')

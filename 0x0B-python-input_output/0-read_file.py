#!/usr/bin/python3
""" how to read a file """

def read_file(filename=""):
    """ method to read a filename file"""
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end='')

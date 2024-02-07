#!/usr/bin/python3
""" Appending txte to file """


def append_write(filename="", text=""):
    """function to append file """
    with open(filename, 'a+', encoding='utf-8') as f:
        return f.write(text)

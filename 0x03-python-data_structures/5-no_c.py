#!/usr/bin/python3

def no_c(my_string):
    for a in my_string:
        if a not in ('cC'):
            print("{}".format(a));

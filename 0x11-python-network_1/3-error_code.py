#!/usr/bin/python3
""" Script to display error using urllib
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            page = r.read().decode('utf-8')
            print(page)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e))

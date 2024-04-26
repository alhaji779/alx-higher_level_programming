#!/usr/bin/python3
# Script to fetch parameter in header
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        data = r.read()
        data2 = r.info()
        val = data2.get('X-Request-Id')
        print(val)

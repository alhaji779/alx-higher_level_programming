#!/urs/bin/python3
""" working with request headers
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    head = r.headers['X-Request-Id']
    print(head)

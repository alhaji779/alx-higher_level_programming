#!/usr/bin/python3
""" Script to access Github api
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auths = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auths)
    print(r.json().get('id'))

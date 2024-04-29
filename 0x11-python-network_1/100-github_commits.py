#!/usr/bin/python3
""" Script to get commits of a particular user
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[1], sys.argv[2])
    r = requests.get(url)
    all_data = r.json()
    for i, j in enumerate(all_data):
        if i == 10:
            break
        else:
            commit = j.get('sha')
            name = j.get('commit').get('author').get('name')
            print("{}: {}".format(commit, name))

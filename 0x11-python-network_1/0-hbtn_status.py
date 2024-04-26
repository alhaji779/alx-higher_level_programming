#!/usr/bin/python3
""" Script to fetch data from a url """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        data = r.read()
        data_ecode = data.decode('utf-8')
        print("Body response:")
        print("\t - type: {}".format(type(data)))
        print("\t - content: {}".format(data))
        print("\t - utf8 content: {}".format(data_ecode))

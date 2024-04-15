#!/usr/bin/python3
""" SCript to select from a table given an argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
              id ASC".format(argv[4]))
    cc = c.fetchall()
    for row in cc:
        print(row)

    c.close()
    db.close()

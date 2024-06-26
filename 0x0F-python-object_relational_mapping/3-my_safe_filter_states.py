#!/usr/bin/python3

""" Scpript to avoid sql-injection """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("Select * from states where name like %s \
              order by id", (argv[4],))
    cc = c.fetchall()
    for row in cc:
        print(row)

    c.close()
    db.close()

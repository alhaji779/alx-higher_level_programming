#!/usr/bin/python3

""" Python code to display all records from states table starting with N """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""Select * from states where name ilike 'N%' order by id """)
    cc = c.fetchall()

    for row in cc:
        print(row)

    c.close()
    db.close()

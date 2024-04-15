#!/usr/bin/python3
""" Script to list cites by states """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT a.id, a.name,b.name from cities a join states \
              b on b.id = a.state_id order by a.id")
    cc = c.fetchall()
    
    for row in cc:
        print(row)

    c.close()
    db.close()

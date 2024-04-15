#!/usr/bin/python3

""" List cities in a state given an argument """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("Select a.name from cities a join states b on b.id \
              = a.state_id where b.name = %s", (argv[4],))
    cc = c.fetchall()
    print(", ".join(row[0] for row in cc))
    c.close()
    db.close()

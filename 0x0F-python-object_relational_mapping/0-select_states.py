#!/usr/bin/python3

""" Python csript to show all records in a given table """

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    c = db.cursor()
    c.execute("""SELECT * from states order by id""")
    cc = c.fetchall()
    for row in cc:
        print(row)

    c.close()
    db.close()

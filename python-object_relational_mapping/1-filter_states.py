#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)
from the database """


import MySQLdb
import sys


if __name__ == "__main__":
    bd = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = bd.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' LIMIT 2")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    bd.close()

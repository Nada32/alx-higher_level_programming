#!/usr/bin/python3
"""
hi
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    hi
    """
    x = MySQLdb.connect (
        host = 3306,
        user = arg[1],
        pw = arg[2],
        database = arg[3]
        )
    cursorObject = dataBase.cursor()
    query = "SELECT * FROM states ORDERED BY states.id"
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)

    dataBase.close()

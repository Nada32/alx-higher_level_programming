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
    dataBase = MySQLdb.connect (
        host = 3306,
        user = argv[1],
        pw = argv[2],
        database = argv[3]
        )
    cursorObject = dataBase.cursor()
    query = "SELECT * FROM states ORDER BY states.id"
    x = cursorObject.execute(query)

    for i in range(x):
        print(cursorObject.fetchone())
    dataBase.close()

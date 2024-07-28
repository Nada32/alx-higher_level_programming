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
    db = MySQLdb.connect (
        host = 3306,
        user = sys.argv[1],
        pw = sys.argv[2],
        db = sys.argv[3]
        )
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(num_rows):
        print(cur.fetchone())

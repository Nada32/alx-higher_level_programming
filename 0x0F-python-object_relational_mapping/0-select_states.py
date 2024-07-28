#!/usr/bin/python3
"""
hi
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    hi
    """
    db = MySQLdb.connect (
        host = "localhost",
        user = sys.argv[1],
        pw = sys.argv[2],
        db = sys.argv[3],
        port = 3306
        )
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(num_rows):
        print(cur.fetchone())

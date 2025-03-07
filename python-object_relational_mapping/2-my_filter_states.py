#!/usr/bin/python3
"""Script that displays values in states table matching argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute query with user input
    query = """SELECT * FROM states
               WHERE BINARY name = '{}'
               ORDER BY id ASC""".format(sys.argv[4])
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

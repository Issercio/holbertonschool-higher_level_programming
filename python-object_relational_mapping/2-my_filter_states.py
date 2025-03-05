#!/usr/bin/python3
"""Script that lists all states from database hbtn_0e_0_usa where name matches argument"""

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

    # Execute query using format
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
                  .format(sys.argv[4]))

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

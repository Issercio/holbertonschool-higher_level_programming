#!/usr/bin/python3
"""Script that lists states starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL with command line arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute query to get states starting with N
    cursor.execute("SELECT * FROM states \
                   WHERE name LIKE 'N%' \
                   ORDER BY id ASC")

    # Fetch and print results
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':  # Double check for binary comparison
            print(state)

    # Close cursor and database
    cursor.close()
    db.close()

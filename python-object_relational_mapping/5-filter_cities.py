#!/usr/bin/python3
"""Script that lists all cities of a state from the database hbtn_0e_4_usa"""

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

    # Execute SQL query with parameterized query to prevent SQL injection
    query = """SELECT cities.name
             FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name = %s
             ORDER BY cities.id ASC"""
    cursor.execute(query, (sys.argv[4],))

    # Fetch all results
    cities = cursor.fetchall()

    # Print results
    print(", ".join([city[0] for city in cities]))

    # Close cursor and database connection
    cursor.close()
    db.close()

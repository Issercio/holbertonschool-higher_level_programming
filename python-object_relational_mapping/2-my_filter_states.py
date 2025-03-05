#!/usr/bin/python3
"""Script that takes argument and lists states"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create the SQL query with the argument passed using format
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query
    cursor.execute(query, (state_name,))

    # Fetch all rows and display them
    results = cursor.fetchall()

    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

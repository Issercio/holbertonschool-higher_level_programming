#!/usr/bin/python3
'''base model for select_states
'''


import MySQLdb
import sys

def list_states():
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute the query to fetch all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states()

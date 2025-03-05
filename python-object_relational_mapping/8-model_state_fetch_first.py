#!/usr/bin/python3
"""Prints first State object from database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create session
    session = Session()
    
    # Query first State object
    first_state = session.query(State).order_by(State.id).first()
    
    # Print result or Nothing if empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    
    # Close session
    session.close()

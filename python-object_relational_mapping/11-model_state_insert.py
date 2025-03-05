#!/usr/bin/python3
"""Adds State object Louisiana to database"""
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
    
    # Create new Louisiana state
    louisiana = State(name="Louisiana")
    
    # Add and commit the new state
    session.add(louisiana)
    session.commit()
    
    # Print the new state's id
    print(louisiana.id)
    
    # Close session
    session.close()

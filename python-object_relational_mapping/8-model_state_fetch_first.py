#!/usr/bin/env python3
"""Script that prints the first State object from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create connection to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                         pool_pre_ping=True)

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query first state
    first_state = session.query(State).order_by(State.id).first()

    # Check if state exists and print
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
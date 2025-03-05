#!/usr/bin/env python3
"""Script that lists all State objects containing letter 'a' from the database"""

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

    # Query states containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()

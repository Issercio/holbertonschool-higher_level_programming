#!/usr/bin/python3
"""Script that prints the State object with given name"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state by name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print state id if found, otherwise print Not found
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

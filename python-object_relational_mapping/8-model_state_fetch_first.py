#!/usr/bin/python3
"""Script that prints the first State object from database"""

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

    # Query first State object
    state = session.query(State).order_by(State.id).first()

    # Print result or Nothing if empty
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()

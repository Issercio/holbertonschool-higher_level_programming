#!/usr/bin/python3
"""Script that lists all State objects containing letter a"""

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

    # Query states containing letter 'a'
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()

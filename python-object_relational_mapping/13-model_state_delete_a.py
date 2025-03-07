#!/usr/bin/python3
"""Script that deletes all State objects with name containing 'a'"""

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

    # Query and delete states containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()

    session.close()

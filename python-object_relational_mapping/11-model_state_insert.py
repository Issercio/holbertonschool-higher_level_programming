#!/usr/bin/python3
"""Script that adds the State object 'Louisiana' to database"""

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

    # Create new State object
    new_state = State(name="Louisiana")

    # Add and commit the new state
    session.add(new_state)
    session.commit()

    # Print new state id
    print(new_state.id)

    session.close()

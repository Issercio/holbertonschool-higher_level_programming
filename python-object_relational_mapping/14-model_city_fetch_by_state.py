#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine that connects to the core of our database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                         pool_pre_ping=True)

    # Create session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query City and State objects and join them
    cities = session.query(City, State)\
        .join(State, City.state_id == State.id)\
        .order_by(City.id).all()

    # Display results
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()

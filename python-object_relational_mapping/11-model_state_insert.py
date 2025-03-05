#!/usr/bin/env python3
# filepath: /root/holbertonschool-higher_level_programming/python-object_relational_mapping/11-model_state_insert.py

"""Script that adds the State object "Louisiana" to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create connection to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create session
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")
    
    # Add the new state to the session
    session.add(new_state)
    
    # Commit the session to save changes
    session.commit()
    
    # Print the new state's id
    print(new_state.id)
    
    # Close the session
    session.close()
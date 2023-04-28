#!/usr/bin/python3
"""
    This is a Script that prints the State object with the
    name passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Set up connection to the database
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    name_to_search = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(db_username, db_password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state with the name passed as argument
    state = session.query(State).filter(State.name == name_to_search).first()

    # Display the result or "Not found"
    if state is None:
        print("Not found")
    else:
        print(state.id)

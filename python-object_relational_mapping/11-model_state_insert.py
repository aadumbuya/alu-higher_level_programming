#!/usr/bin/python3
"""
    This is a script that adds the State object
    "Louisiana" to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session object
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new states.id
    print(new_state.id)

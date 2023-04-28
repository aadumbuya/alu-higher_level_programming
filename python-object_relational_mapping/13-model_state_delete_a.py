#!/usr/bin/python3
"""
    This is a script thst deletes all State objects
    with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Connection settings
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    connection_settings = {
        'host': 'localhost',
        'port': 3306,
        'user': db_user,
        'passwd': db_password,
        'db': db_name,
        'charset': 'utf8'
    }

    # Create connection
    engine = create_engine('mysql+mysqldb://{user}:{passwd}@{host}:{port}/{db}'
                           .format(**connection_settings))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all states with a name containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()

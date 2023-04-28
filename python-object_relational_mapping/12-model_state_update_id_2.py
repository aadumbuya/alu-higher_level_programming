#!/usr/bin/python3
"""
    This is a Changes the name of a State object from
    the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get the connection arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    # Open a connection to the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(mysql_user, mysql_passwd, mysql_db),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with id=2
    state = session.query(State).filter_by(id=2).first()

    # If the state exists, change its name to New Mexico
    if state:
        state.name = 'New Mexico'
        session.commit()
    else:
        print('Not found')

    # Close the session
    session.close()

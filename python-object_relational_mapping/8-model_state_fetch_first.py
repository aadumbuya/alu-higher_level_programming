#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).first()
    if query:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")

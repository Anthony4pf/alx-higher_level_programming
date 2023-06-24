#!/usr/bin/python3
"""This module lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
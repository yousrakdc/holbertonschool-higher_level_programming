#!/usr/bin/python3
"""  lists all State objects that contain the letter 'a' """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    db_session = Session()

for state in db_session.query(State)\
                       .filter(State.name.like('%a%'))\
                       .order_by(State.id)\
                       .all():
    print("{}: {}".format(state.id, state.name))

    db_session.close()

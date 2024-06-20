#!/usr/bin/python3
"""prints the State object with the name passed as argument from database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    db_session = Session()

    state = db_session.query(State)\
        .filter(State.name == sys.argv[4])\
        .first()

    if state:
        print(state.id)
    else:
        print("Not found")

    db_session.close()

#!/usr/bin/python3
"""changes the name of a State object from the database"""

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    db_session = Session()
    db_session = Session()
    db_session.query(State).filter(
        State.id == 2).update({"name": "New Mexico"})
    db_session.commit()
    db_session.close()

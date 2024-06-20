#!/usr/bin/python3
"""deletes all State objects with a name containing the letter 'a'
from the database"""

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
    db_session.query(State).filter(State.name.like('%a%')).delete()
    db_session.commit()
    db_session.close()

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

    db_session.add(State(name="Louisiana"))
    db_session.commit()
    louisiana = db_session.query(State).filter(State.name ==
                                               "Louisiana").first()

    print(louisiana.id)
    db_session.close()

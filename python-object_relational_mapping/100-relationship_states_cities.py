#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”
from the database """

from sys import argv, exit
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    if len(argv) != 4:
        exit('Use: 100-relationship_states_cities.py <mysql username> '
             '<mysql password> <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    db_session = Session()
    Base.metadata.create_all(engine)

    new_state = State(name='California')
    new_city = City(name='San Francisco', state_id=new_state.id)
    new_state.cities.append(new_city)
    db_session.add_all([new_state, new_city])

    db_session.commit()
    db_session.close()

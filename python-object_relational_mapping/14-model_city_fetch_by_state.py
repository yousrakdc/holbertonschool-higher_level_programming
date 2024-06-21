#!/usr/bin/python3
"""Start link class to table in database """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    db_session = Session()

    # Querying the database to join City & State tables and ordering by City.id
    for city, state in (db_session.query(City, State)
                        .join(State, City.state_id == State.id)
                        .order_by(City.id)):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    db_session.close()

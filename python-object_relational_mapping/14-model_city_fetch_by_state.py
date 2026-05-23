#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities joined with states
    results = session.query(State, City).join(City, State.id == City.state_id)\
                .order_by(City.id).all()

    # Print formatted output
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
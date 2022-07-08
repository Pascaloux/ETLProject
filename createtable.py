from base import Base, engine
from tables import ValeursFoncieres


if __name__ == "__main":  
    Base.metadata.create_all(engine)
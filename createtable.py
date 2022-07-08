from base import Base, engine
from table import ValeursFoncieres


if __name__ == "__main":  
    Base.metadata.create_all(engine)
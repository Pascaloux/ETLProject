from base import Base, engine
from table import*


if __name__ == "__main":  
    Base.metadata.create_all(engine)
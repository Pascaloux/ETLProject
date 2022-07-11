from base import Base, engine
from table import *


if __name__ == "__main__":  
    Base.metadata.create_all(engine)
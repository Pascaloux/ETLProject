from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *
from table import *


def load(df):
    print("Chargement des valeurs foncières")
    result=df.to_dict('records')
    
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in result:
        row = ValeursFoncieres(**item)
        session.add(row)

    session.commit()
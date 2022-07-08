from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *


def load(df):
    print("Chargement des valeurs foncières")
    test=df.to_dict('records')
    print(test)
from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *
from table import *


def load_valeur_fonciere(df):
    print("Chargement des valeurs foncières")
    result=df.to_dict('records')
    
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in result:
        row = ValeursFoncieres(**item)
        session.add(row)

    session.commit()

def load_taux(df):
    dico=df.to_dict("records")
    liste_index=df.index
    for i in range(len(dico)):
        dico[i]["devise"]=liste_index[i]

    for taux in dico:
        row = Taux(devise=taux['devise'],valeur=taux['rates'])
        session.add(row)
    session.commit()

def load_Capitaux(data):
    result = [{col:getattr(row, col) for col in data} for row in data.itertuples()]
    for item in result:
        row = Bank_capitalisation(Name=item['Name'], Market_Cap = item['Market_Cap_Euro_Billion'] )
        session.add(row)
    session.commit()
    
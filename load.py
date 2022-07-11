from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *
from base import *
from table import *
from tqdm import tqdm


def load_date_valeurs_foncieres(date):
    print("Chargement de la date des valeurs foncières")

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(DateValeursFoncieres(DateMAJ=date))

    session.commit()


def load_valeurs_foncieres(df):

    print("Chargement des valeurs foncières")
    result=df.to_dict('records')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Dictionnaire chargé")
    for item in tqdm(result):
        row = ValeursFoncieres( NoDisposition = item['No disposition'],
                                DateMutation = item['Date mutation'],
                                NatureMutation = item['Nature mutation'],
                                ValeurFonciere = item['Valeur fonciere'],
                                NoVoie = item['No voie'],
                                BTQ = item['B/T/Q'],
                                TypeVoie = item['Type de voie'],
                                CodeVoie = item['Code voie'],
                                Voie = item['Voie'],
                                CodePostal = item['Code postal'],
                                Commune = item['Commune'],
                                CodeDepartement = item['Code departement'],
                                CodeCommune = item['Code commune'],
                                PrefixeSection = item['Prefixe de section'],
                                Section = item['Section'],
                                NoPlan = item['No plan'],
                                NoVolume = item['No Volume'],
                                Lot1 = item['1er lot'],
                                CarrezLot1 = item['Surface Carrez du 1er lot'],
                                Lot2 = item['2eme lot'],
                                CarrezLot2 = item['Surface Carrez du 2eme lot'],
                                Lot3 = item['3eme lot'],
                                CarrezLot3 = item['Surface Carrez du 3eme lot'],
                                Lot4 = item['4eme lot'],
                                CarrezLot4 = item['Surface Carrez du 4eme lot'],
                                Lot5 = item['5eme lot'],
                                CarrezLot5 = item['Surface Carrez du 5eme lot'],
                                NombreLots = item['Nombre de lots'],
                                CodeTypeLocal = item['Code type local'],
                                TypeLocal = item['Type local'],
                                SurfaceReelleBati = item['Surface reelle bati'],
                                NombrePiecesPrincipales = item['Nombre pieces principales'],
                                NatureCulture = item['Nature culture'],
                                NatureCultureSpeciale = item['Nature culture speciale'],
                                SurfaceTerrain = item['Surface terrain']
                                )
        session.add(row)
        

    session.commit()


def load_taux(df):
    dico=df.to_dict("records")
    liste_index=df.index
    for i in range(len(dico)):
        dico[i]["devise"]=liste_index[i]

    for taux in dico:
        row = Taux(devise=taux['devise'],valeur=taux['rates'])
        print(row)
        session.add(row)
    session.commit()


def load_Capitaux(data):
    result = [{col:getattr(row, col) for col in data} for row in data.itertuples()]
    for item in result:
        row = Bank_capitalisation(Name=item['Name'], Market_Cap = item['Market_Cap_Euro_Billion'] )
        session.add(row)
    session.commit()
    
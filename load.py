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
        row = Taux_temp(devise=taux['devise'],valeur=taux['rates'])
        print(row)
        session.add(row)
    session.commit()

    clean_transaction_ids = session.query(Taux_final.transaction_id)
    transaction_to_insert = session.query(Taux_temp).filter(~Taux_temp.transaction_id.in_(clean_transaction_ids))

    liste_donnee =[]
    for row in transaction_to_insert:
        dico_final={}
        dico_final["devise"] = row.devise
        dico_final["valeur"]= row.valeur
        liste_donnee.append(dico_final)


    for taux in liste_donnee:
        row = Taux_final(**taux)
        session.add(row)
session.commit()




def load_Capitaux(data):
    result = [{col:getattr(row, col) for col in data} for row in data.itertuples()]
    for item in result:
        row = Bank_cap_temp(Name=item['Name'], Market_Cap = item['Market_Cap_Euro_Billion'] )
        session.add(row)
    session.commit()
    clean_id = session.query(Bank_cap_final.identifier)
    id_to_insert = session.query(Bank_cap_temp).filter(~Bank_cap_temp.identifier.in_(clean_id))
    liste_donnee =[]
    for row in id_to_insert:
        dico_final={}
        dico_final["Name"] = row.Name
        dico_final["Market_Cap"]= row.Market_Cap
        liste_donnee.append(dico_final)
    for item in liste_donnee:
        row = Bank_cap_final(**item )
        session.add(row)
    session.commit()
    raw_id = session.query(Bank_cap_temp.identifier)
    id_to_delete = session.query(Bank_cap_final).filter(~Bank_cap_final.identifier.in_(raw_id))
    liste_donnee =[]
    for row in id_to_delete:
        dico_final={}
        dico_final["Name"] = row.Name
        dico_final["Market_Cap"]= row.Market_Cap
        liste_donnee.append(dico_final)
    for item in liste_donnee:
        row = Bank_cap_final(**item )
        session.delete(row)
    session.commit()
    Bank_cap_temp.__table__.drop(engine)


    
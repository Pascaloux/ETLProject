# Import des librairies
import pandas as pd
import numpy as np

def transform(df):
    # Suppression des colonnes vides
    df = df.drop(['Code service CH','Reference document','1 Articles CGI','2 Articles CGI','3 Articles CGI','4 Articles CGI','5 Articles CGI','Identifiant local'], axis=1)

    # Changer le type des colonnes alphanumériques en string
    df['Nature mutation']           = df['Nature mutation'].astype('string')
    df['B/T/Q']                     = df['B/T/Q'].astype('string')
    df['Type de voie']              = df['Type de voie'].astype('string')
    df['Code voie']                 = df['Code voie'].astype('string')
    df['Voie']                      = df['Voie'].astype('string')
    df['Commune']                   = df['Commune'].astype('string')
    df['Code departement']          = df['Code departement'].astype('string')
    df['Section']                   = df['Section'].astype('string')
    df['No Volume']                 = df['No Volume'].astype('string')
    df['1er lot']                   = df['1er lot'].astype('string')
    df['2eme lot']                  = df['2eme lot'].astype('string')
    df['3eme lot']                  = df['3eme lot'].astype('string')
    df['4eme lot']                  = df['4eme lot'].astype('string')
    df['5eme lot']                  = df['5eme lot'].astype('string')
    df['Type local']                = df['Type local'].astype('string')
    df['Nature culture']            = df['Nature culture'].astype('string')
    df['Nature culture speciale']   = df['Nature culture speciale'].astype('string')
    df['Surface Carrez du 1er lot']   = df['Surface Carrez du 1er lot'].astype('string')

    # Changer le type des colonnes numériques avec uniquement des entiers en int64
    df['No voie']               = df['No voie'].replace(np.nan, 0).astype('int64')
    df['Code postal']           = df['Code postal'].replace(np.nan, 0).astype('int64')
    df['Prefixe de section']    = df['Prefixe de section'].replace(np.nan, 0).astype('int64')
    df['No plan']               = df['No plan'].replace(np.nan, 0).astype('int64')

    # Changer le type des colonnes numériques avec des chiffres à virgules en float
    df['Valeur fonciere']               = df['Valeur fonciere'].str.replace(',', '.', regex=True).astype('float')
    df['Surface Carrez du 1er lot']     = df['Surface Carrez du 1er lot'].str.replace(',', '.', regex=True).astype('float')
    df['Surface Carrez du 2eme lot']    = df['Surface Carrez du 2eme lot'].str.replace(',', '.', regex=True).astype('float')
    df['Surface Carrez du 3eme lot']    = df['Surface Carrez du 3eme lot'].str.replace(',', '.', regex=True).astype('float')
    df['Surface Carrez du 4eme lot']    = df['Surface Carrez du 4eme lot'].str.replace(',', '.', regex=True).astype('float')
    df['Surface Carrez du 5eme lot']    = df['Surface Carrez du 5eme lot'].str.replace(',', '.', regex=True).astype('float')

    return df
# Import des librairies
import pandas as pd


def extract():
    # Lien des valeurs foncières en 2021
    url = 'https://www.data.gouv.fr/fr/datasets/r/817204ac-2202-4b4a-98e7-4184d154d98c'

    # Enregistrement des données dans un dataframe avec le bon format date
    df = pd.read_csv(url, delimiter='|', parse_dates=['Date mutation'], dayfirst=True)

    return df







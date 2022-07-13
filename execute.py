import extract
import transform
import load

# Extraction des données
date = extract.extract_date_valeurs_foncieres()
df_raw  = extract.extract_valeurs_foncieres()
df_raw_capitaux = extract.extract_capitaux()

#Transformation des données
df_prep = transform.transform_valeurs_foncieres(df_raw)
df_prep_capitaux=transform.transform_capitaux(df_raw_capitaux,df_taux)

# Chargement des données
load.load_date_valeurs_foncieres(date)
load.load_valeurs_foncieres(df_prep)
load.load_valeurs_foncieres(df_prep_capitaux)

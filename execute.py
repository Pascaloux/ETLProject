import extract
import transform
import load

# Extraction des données
date = extract.extract_date_valeurs_foncieres()
df_raw  = extract.extract_valeurs_foncieres()

#Transformation des données
df_prep = transform.transform_valeurs_foncieres(df_raw)

# Chargement des données
load.load_date_valeurs_foncieres(date)
load.load_valeurs_foncieres(df_prep)

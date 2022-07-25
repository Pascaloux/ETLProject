import extract
import transform
import load

# Extraction des données
date = extract.extract_date_valeurs_foncieres()
df_raw  = extract.extract_valeurs_foncieres()
df_raw_taux = extract.extract_taux()
df_raw_capitaux = extract.extract_capitaux()

#Transformation des données
df_prep = transform.transform_valeurs_foncieres(df_raw)
df_prep_taux=transform.transform_taux(df_raw_taux)
df_prep_capitaux=transform.transform_capitaux(df_raw_capitaux,df_prep_taux)

# Chargement des données
load.load_date_valeurs_foncieres(date)
load.load_valeurs_foncieres(df_prep)
load.load_taux(df_prep_taux)
load.load_Capitaux(df_prep_capitaux)
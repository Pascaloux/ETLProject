import extract
import transform
import load


df_raw  = extract.extract_valeurs_Foncieres()
df_prep = transform.transform_valeurs_Foncieres(df_raw)
load.load(df_prep)

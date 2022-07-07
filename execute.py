import extract
import transform
import load
import pandas as pd
import numpy as np

df_raw  = extract.extract_valeurs_Foncieres()
df_prep = transform.transform_valeurs_Foncieres(df_raw)

<<<<<<< Updated upstream
print(df_prep)

print("okkk")
=======

print(df_prep)

l = (pd.unique(df_prep['Surface Carrez du 1er lot'].replace(np.nan,' ')))
l2 = [item for item in l if not isinstance(item, float)]
print(l2)
#print(sorted(pd.unique(df_prep['Section'].replace(np.nan,' '))))
#print(sorted(pd.unique(df_prep['No plan'])))

#print(sorted(pd.unique(df_prep['Code voie'].replace(np.nan,' '))))

#load.load(df_prep)
>>>>>>> Stashed changes

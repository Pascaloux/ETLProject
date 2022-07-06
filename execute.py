import extract
import transform
import load

df_raw  = extract.extract()
df_prep = transform.transform(df_raw)

print(df_prep)
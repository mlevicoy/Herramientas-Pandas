import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Creamos la columna NACIONALIDADN y la rellenamos con CHILE
df["NACIONALIDAD"] = "CHILE"

print(df)
# Eliminamos la columna NACIONALIDAD
del df["NACIONALIDAD"]

print(df)
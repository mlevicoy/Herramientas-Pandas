import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Creamos una columna a partir de la operación de otras
# dos columnas
df["BONO"] = df["MONTO"]/df["PUNTAJE_CREDITICIO"]

print(df)
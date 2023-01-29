import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Mostramos la fecha de nacimiento en esa línea
print(df.loc[658]["FECHA_NAC"])
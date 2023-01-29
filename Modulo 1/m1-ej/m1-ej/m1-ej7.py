import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Mostramos varias filas
print(df.loc[100:105])
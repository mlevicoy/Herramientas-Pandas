import pandas as pd

df_clientes = pd.read_csv("clientes.csv",encoding="latin-1", sep=";")

print(df_clientes)

print(df_clientes.dtypes)
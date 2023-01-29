import pandas as pd
import numpy as np

df_clientes = pd.read_csv("C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\clientes.csv", encoding="latin-1", sep=";")
print(df_clientes)
print(df_clientes.dtypes)
df_clientes["FECHA_NAC"] = df_clientes["FECHA_NAC"].str.replace("/", "-")
print(df_clientes)

print("1: ")
print(df_clientes.loc[(df_clientes["MONTO"] > 1000000) & (df_clientes["MONTO"] < 1500000)])

print("2: ")
print(df_clientes.loc[(df_clientes["MONTO"] > 3000000) | (df_clientes["MONTO"] < 500000)])

print("3: ")
print(df_clientes.loc[df_clientes["RUT"].str.contains("-K")])
print(df_clientes.loc[df_clientes["RUT"].str[-1:] == "4"])

print("4: ")
print(df_clientes.loc[df_clientes["NOMBRE"].str.split(" ", expand=True)[3] == "Ruiz"])

print("5: ")
print(df_clientes.loc[(df_clientes["NOMBRE"].str.split(" ", expand=True)[2] == "López") & 
(df_clientes["TIPO_CLIENTE"] == "C")])

print("6: ")
print(df_clientes.loc[(df_clientes["RUT"].str.contains("-4")) | (df_clientes["TIPO_CLIENTE"] == "A") & (df_clientes["MONTO"] > 1000000)])

print("7: ")
df_clientes = df_clientes.sort_values(by=["TIPO_CLIENTE", "MONTO"], ascending=False)
print(df_clientes)

df_clientes["RUT"].str.replace("/","")

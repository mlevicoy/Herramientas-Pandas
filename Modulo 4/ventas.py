import pandas as pd
import numpy as np

df_ventas = pd.read_csv(
    "C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\ventas.csv", 
    encoding="latin-1", sep=";"  
)

df_ventas["FECHA"] = df_ventas["FECHA"].str.replace("=", "/")

df_ventas["NUM"] = df_ventas["NUM"].str.replace(" ", "")
df_ventas["NUM"] = df_ventas["NUM"].str.replace(".", "")
df_ventas["NUM"] = df_ventas["NUM"].str.replace(",", "")

print(df_ventas.head())

df_lista_productos = pd.read_csv(
    "C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\lista_productos.csv",
    encoding="latin-1", sep=","
)

"""Verificamos los tipos de datos"""
print("DF_VENTAS: (ventas.csv)")
print(df_ventas.dtypes)
print("DF_LISTA_PRODUCTOS: (lista_productos.csv)")
print(df_lista_productos.dtypes)

df_lista_productos["NUM"] = df_lista_productos["NUM"].astype(str)
print(df_lista_productos.dtypes)

df_ventas = df_ventas.merge(df_lista_productos, on="NUM")
print(df_ventas)






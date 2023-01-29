import pandas as pd
import numpy as np

#MÓDULO 2
df_consultas = pd.read_csv("consultas.csv",sep=";")
print(df_consultas.dtypes)

#2
df_consultas["Fecha_Hora_Consulta"]=df_consultas["Fecha_Hora_Consulta"].astype("datetime64")
print(df_consultas.dtypes)

#3
print(df_consultas.shape)
print(df_consultas.size)

#4
df_consultas = df_consultas.set_index("RUT")

#5
print(df_consultas.head())
print(df_consultas.tail())

#6a
print(df_consultas.loc["6.079.686-2"])

#6b
print(df_consultas.loc["4.367.282-7":"19.500.328-3"])

#6c
print(df_consultas.iloc[23])

#6d
print(df_consultas.iloc[76:89])

#7
df_consultas = df_consultas.rename(columns={"Fecha_Hora_Consulta":"Fecha_Consulta","RUT2":"RUT_medico"})
print(df_consultas.dtypes)

#8
print(df_consultas)
df_consultas = df_consultas.fillna("10000")
print(df_consultas)

#9
print(df_consultas.size)
df_consultas2 = pd.read_csv("consultas2.csv",sep=";")
df_consultas2["Fecha_Hora_Consulta"]=df_consultas2["Fecha_Hora_Consulta"].astype("datetime64")
df_consultas2 = df_consultas2.set_index("RUT")
df_consultas2 = df_consultas2.rename(columns={"Fecha_Hora_Consulta":"Fecha_Consulta","RUT2":"RUT_medico"})
df_consultas=df_consultas.append(df_consultas2)
print(df_consultas.size)

#10
print(df_consultas.iloc[0:10])
print(df_consultas.shape)
df_consultas = df_consultas.drop(df_consultas.iloc[0:10].index)
print(df_consultas.iloc[0:10])
print(df_consultas.shape)
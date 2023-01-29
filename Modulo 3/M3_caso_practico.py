import pandas as pd
import numpy as np

df_pacientes = pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")
print(df_pacientes)

#MÓDULO 3
#1
lista_montos = []
for index,row in df_pacientes.iterrows():
	valor = row["Monto_Deuda"]
	valor /= 700
	lista_montos.append(valor)

print(lista_montos[0:10])

#2
print(df_pacientes["Nombre"].str[0:10])

#3
df_pacientes["Nombre"] = df_pacientes["Nombre"].str.upper()
print(df_pacientes.head())

#4
print(df_pacientes.loc[df_pacientes["Nombre"].str.contains("Ñ")])

#5
df_pacientes2 = pd.read_csv("datos_pacientes2.csv",encoding="utf-8",sep=";")

#6
print(df_pacientes2)
df_pacientes2 = df_pacientes2.loc[~(df_pacientes2["RUT"].str.contains("XXXX")) & ~(df_pacientes2["Nombre"].str.contains("XXXX"))]
print(df_pacientes2)

#7
print(df_pacientes2)
df_pacientes2["Nombre"] = df_pacientes2["Nombre"].str.replace("-"," ")
print(df_pacientes2)

#8
print(df_pacientes2)
df_pacientes2["Fecha_Nacimiento"] = df_pacientes2["Fecha_Nacimiento"].str.replace("_/","/")
print(df_pacientes2)

#9
print(df_pacientes.tail())
df_pacientes = df_pacientes.append(df_pacientes2)
print(df_pacientes.tail())

#10
df_pacientes = df_pacientes.set_index("RUT")
print(df_pacientes)

#11
df2 = df_pacientes["Nombre"].str.split(" ",expand=True)
df2.columns=["Primer Nombre","Segundo Nombre","Primero Apellido","Segundo Apellido"]
print(df2)
df_pacientes = df_pacientes.join(df2)
print(df_pacientes.shape)
print(df_pacientes.head())
#12
df_nacionalidad = pd.read_csv("nacionalidad.csv",encoding="utf-8",sep=";")
df_pacientes = df_pacientes.merge(df_nacionalidad,left_index=True,right_on="RUT",how="left")
df_pacientes = df_pacientes.set_index("RUT")
print(df_pacientes.dtypes)
print(df_pacientes.head())
print(df_pacientes)
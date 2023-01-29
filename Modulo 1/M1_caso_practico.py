import pandas as pd
import numpy as np

#MÓDULO 1
#2
df_pacientes = pd.read_csv("datos_pacientes.csv",encoding="utf-8",sep=";")
print(df_pacientes)

#3a
print(df_pacientes["Monto_Deuda"])

#3b
print(df_pacientes.loc[651])

#3c
print(df_pacientes.loc[100:200])
print(df_pacientes.loc[100:200]["RUT"])
print(df_pacientes.loc[100:200]["Nombre"])

#3d
print(df_pacientes.loc[df_pacientes["Previsión"] == "FONASA"])

#3e
print(df_pacientes.loc[df_pacientes["Monto_Deuda"] > 1000000])

#4
df_pacientes["Nacionalidad"] = "CHILE"
print(df_pacientes)

#5
df_pacientes["Monto_Deuda"] = df_pacientes["Monto_Deuda"]*1.03
print(df_pacientes)

#6
del df_pacientes["Nacionalidad"]

#7
print(df_pacientes.describe())

#8
df_pacientes.to_csv("datos_pacientes_reajustado.csv",sep=";",index=False)
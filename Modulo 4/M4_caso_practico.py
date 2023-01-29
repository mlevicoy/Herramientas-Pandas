import pandas as pd
import numpy as np

#MÓDULO 4
#1
print(df_pacientes.dtypes)
print(df_pacientes.loc[df_pacientes["País_origen"] != "Chile"])
#2
print(df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"]>1000000)])
#3
print(df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"]>1000000) & (df_pacientes["Previsión"] == "FONASA")])
#4
print(df_pacientes.loc[(df_pacientes["País_origen"] == "Chile") & ((df_pacientes["Ciudad_Residencia"] == "Santiago") | (df_pacientes["Ciudad_Residencia"] == "Concepción")) & (df_pacientes["Monto_Deuda"]>1000000) & (df_pacientes["Previsión"] == "FONASA")])
#5
df_pacientes3 = pd.read_csv("datos_pacientes3.csv",sep=";")
print(df_pacientes3.head())
#6
df_pacientes3 = df_pacientes3.loc[df_pacientes3["RUT"].str[-1:] != "J"]
print(df_pacientes3.head())
#7
print(df_pacientes)
#df_pacientes = df_pacientes.set_index("RUT")
df_pacientes3 = df_pacientes3.set_index("RUT")
df_pacientes = df_pacientes.append(df_pacientes3)
print(df_pacientes)
#8
df_pacientes3 = df_pacientes3.sort_values(by=["Monto_Deuda","Fecha_Nacimiento"],ascending=True)
print(df_pacientes3.head())
#9
pt = df_pacientes3.pivot_table(index="Previsión",values="Monto_Deuda",aggfunc={np.mean,np.min,np.max})
print(pt)
#10
print(df_consultas)
print(df_consultas.dtypes)
df_consultas["Costo_consulta"] = df_consultas["Costo_consulta"].astype("int64")
pt2 = df_consultas.pivot_table(index="RUT_medico",values="Costo_consulta",aggfunc=np.sum)
print(pt2)
#11
df_consultas = df_consultas.merge(pt2,left_on="RUT_medico",right_on="RUT_medico",how="left")
print(df_consultas)

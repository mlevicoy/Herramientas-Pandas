# importamos la libreria
import pandas as pd

# creamos el dataframe
#df_pacientes = pd.read_csv("D:\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\datos_pacientes.csv", encoding="utf-8", sep=";")
#df_nacionalidad = pd.read_csv("D:\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\nacionalidad.csv", encoding="utf-8", sep=";")
df_pacientes = pd.read_csv("C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\datos_pacientes.csv", encoding="utf-8", sep=";")
df_nacionalidad = pd.read_csv("C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\nacionalidad.csv", encoding="utf-8", sep=";")
print(df_pacientes)
print(df_nacionalidad)

# creamos dataframe con los nombre
df_nombres = df_pacientes["Nombre"].str.split(" ", expand=True)
df_nombres.columns = ["Primer Nombre", "Segundo Nombre", "Tercer Nombre", "Cuarto Nombre"]
print(df_nombres)

# unimos los dataframe (df_pacientes y df_nombres)
df_pacientes = df_pacientes.join(df_nombres)
print(df_pacientes)

# unimos los dataframe (df_pacientes y df_nacionalidad)
df_pacientes = df_pacientes.merge(df_nacionalidad, left_on="RUT", right_on="RUT", how="left")
print(df_pacientes)

#1 - En df_pacientes, filtra a los pacientes que no sean de Chile
print(df_pacientes.loc[df_pacientes["País_origen"] != "Chile"])

#2 - En df_pacientes , filtra a los pacientes que no sean de Chile y que tengan una deuda mayor a $1.000.000
print(df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"] > 1000000)])

#3 - En df_pacientes , filtra a los pacientes que no sean de Chile y que tengan una deuda mayor a $1.000.000 
# y que tengan previsión FONASA
print(df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"] > 1000000) & 
(df_pacientes["Previsión"] == "FONASA")])

#4 - En df_pacientes , filtra a los pacientes que sean de Chile pero solo de las ciudades de Santiago o Concepción, 
# que tengan una deuda mayor a $1.000.000 y previsión FONASA.
print(df_pacientes.loc[(df_pacientes["País_origen"] == "Chile") & 
((df_pacientes["Ciudad_Residencia"] == "Santiago") | (df_pacientes["Ciudad_Residencia"] == "Concepción")) & 
(df_pacientes["Monto_Deuda"] > 1000000) & (df_pacientes["Previsión"] == "FONASA")])

#5 - Llegó una nueva base de datos de pacientes. Carga esta información dn df_pacientes3
df_pacientes3 = pd.read_csv("C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\datos_pacientes3.csv", encoding="utf-8", sep=";")
print(df_pacientes3.dtypes)

#6 - Hay pacientes con RUT terminado en J (se asume que son filas creadas por error). Elimina estas filas de df_pacientes3
#print(df_pacientes3.loc[df_pacientes3["RUT"].str.contains("J")])
#df_pacientes3 = df_pacientes3.drop(df_pacientes3.loc[df_pacientes3["RUT"].str.contains("J")].index)
df_pacientes3 = df_pacientes3.loc[df_pacientes3["RUT"].str[-1:] != "J"]
#print(df_pacientes3.loc[df_pacientes3["RUT"].str.contains("J")])
print(df_pacientes3)

#7 - Es necesario unir df_paciente3 a df_pacientes
print("--- datos_pacientes.csv ---")
print(df_pacientes.dtypes)
print("--- datos_pacientes3.csv ---")
print(df_pacientes3.dtypes)
df_pacientes = df_pacientes.set_index("RUT")
df_pacientes3 = df_pacientes3.set_index("RUT")
# append porque son columnas del mismo nombre
df_pacientes = df_pacientes.append(df_pacientes3)
print(df_pacientes)

#8 - Ordenar df_pacientes de forma ascendentes mediante la columna "Monto_Deuda" y "Fecha_Nacimiento" (en ese orden)
df_pacientes = df_pacientes.sort_values(by=["Monto_Deuda", "Fecha_Nacimiento"], ascending=True)
print(df_pacientes)

#9 - Extraer la media, mínimo y máximo de la deuda por tipo de previsión mediante una pivot table
import numpy as np
pt = df_pacientes.pivot_table(index="Previsión", values="Monto_Deuda", aggfunc={np.mean, np.min, np.max})
print(pt)

#10 - Haz un pivot table, por RUT del médico, con la suma de cada consulta
df_consultas = pd.read_csv("C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\consultas.csv", encoding="utf-8", sep=";")
print(df_consultas.dtypes)
#df_consultas["Costo_consulta"] = df_consultas["Costo_consulta"].astype("int64")
pt2 = df_consultas.pivot_table(index="RUT", values="Costo_consulta", aggfunc=np.sum)
print(pt2)

#11 - Haz un merge de esta información, mediante el RUT de cada médico, con df_consultas
df_consultas = df_consultas.merge(pt2, left_on="RUT", right_on="RUT", how="left", suffixes=("_(pacientes)", "_(medicos)"))
print(df_consultas)





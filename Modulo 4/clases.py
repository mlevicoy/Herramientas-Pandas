import pandas as pd
import numpy as np

df = pd.read_csv(
    "C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\ejemplo.csv", 
    encoding="latin-1", sep=";")

print(df.loc[df["Monto"] > 5000000])

print(df.loc[(df["Monto"] >= 5000000) & (df["Monto"] <= 7000000)])

print(df.loc[(df["Monto"] < 1000000) | (df["Monto"] > 9000000)])

print(df.loc[df["Nombre"].str.contains("González")])

# Buscar aquellas personas cuyo primer nombre es Daniela
print(df.loc[df["Nombre"].str.split(" ", expand=True)[0] == "Daniela"])

# Personas de 1er nombre Daniela, digito verificador 8 y un monto menor a 
# $1000000
print(
    df.loc[(df["Nombre"].str.split(" ", expand=True)[0] == "Daniela") & 
    (df["Monto"] < 1000000) & (df["RUT"].str[-1:] == "8")]
)

# Ordenar de forma descendente
df = df.sort_values(by=["Sexo", "Monto"], ascending=False)
print(df)

df = pd.read_csv(
    "C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 4\\ejemplo2.csv", 
    encoding="latin-1", sep=";")

#df2 = df.pivot(index="RUT", columns="BANCO", values="MONTO")
#print(df2)

#df2 = df.pivot_table(index="BANCO", values="MONTO", columns="SEXO", aggfunc=np.mean)
#print(df2)

print("sdf")
"""
df2 = df.pivot_table(index="BANCO", values="MONTO", columns="SEXO", aggfunc={np.mean, np.min, np.max})
print(df2)
"""





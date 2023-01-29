# Cargamos la libreria
import pandas as pd

# Creamos el dataframe a traves de un fichero csv
df = pd.read_csv("ejemplo.csv", encoding="latin-1", sep=";")

# Recorremos el dataframe mostrando el index y el nombre completo
for index, row in df.iterrows():
    print(index)
    print(row["Nombre"])

# Hacemos un split para mostrar solo el nombre
for index,row in df.iterrows():
    primer_nombre = row["Nombre"].split(" ")[0]
    print(primer_nombre)

# Función len()
print(df["Nombre"].str.len())

# Extraer carácter
print(df["RUT"].str[0])

# Extraer caracteres
print(df["RUT"].str[0:4])

# Función lower()
print(df["Nombre"].str.lower())

# Función upper()
print(df["Nombre"].str.upper())

# Función replace(x,y)
print(df["Fecha_Nac"].str.replace("/", "-"))

# Función contains(x)
print(df["RUT"].str.contains("-"))

# Función find(x)
print(df["Nombre"].str.find(" "))

# Función split(x)
print(df["Nombre"].str.split(" "))

# Función split(x, expand=True)
# Crea un dataframe de una columna
df2 = df["Nombre"].str.split(" ", expand=True)
print(df2)

# Cambiamos los nombres de las columnas
df3 = df["Nombre"].str.split(" ", expand=True)
df3.columns = ["Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido"]
print(df3)

# Función join()
df = df.join(df3)
print(df.dtypes)

# Función join(), pero evitando errores de columnas repetidas
df = df.join(df3, rsuffix="_df3", lsuffix="_df3")
print(df.dtypes)

# Función join(), unir dataframe diferentes, rellena con NaN
df4 = pd.DataFrame([["1", 2], ["3", 4]])
df = df.join(df4)
print(df)

# Función merge()
df_banco_A = pd.read_csv("bancoA.csv", encoding="latin-1", sep=";")
df_banco_B = pd.read_csv("bancoB.csv", encoding="latin-1", sep=";")
df_banco_A = df_banco_A.merge(df_banco_B, on="RUT", suffixes=("_bancoA", "_bancoB"))
print(df_banco_A)








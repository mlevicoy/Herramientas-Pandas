import pandas as pd

df = pd.read_csv(
    "C:\\Users\\mlevi\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 3\\ejemplo.csv",
    encoding="latin-1",
    sep=";"
    )

for index,row in df.iterrows():
    print(index)
    print(row["RUT"])

print(df["Nombre"].str.len())

print(df["RUT"].str[3])

print(df["RUT"].str[0:4])

print(df["Nombre"].str.lower())

print(df["Nombre"].str.upper())

print(df["Fecha_Nac"].str.replace("/", "-"))

print(df["RUT"].str.contains("-"))

print(df["Nombre"].str.find(" "))

print(df["Nombre"].str.split(" "))

df2 = df["Nombre"].str.split(" ", expand=True)
df2.columns = ["Primer Nombre", "Segundo Nombre", "Primero Apellido", "Segundo Apellido"]
print(df2)

df = df.join(df2)
print(df)

df = df.join(df2, rsuffix="_df2", lsuffix="_df")
print(df.dtypes)

df_banco_A = pd.read_csv(
    "C:\\Users\\mlevi\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 3\\bancoA.csv",
    encoding="latin-1",
    sep=";"
)
df_banco_B = pd.read_csv(
    "C:\\Users\\mlevi\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 3\\bancoB.csv",
    encoding="latin-1",
    sep=";"
)

#df_banco_A = df_banco_A.merge(df_banco_B, on="RUT", suffixes=("_bancoA", "bancoB"))
#print(df_banco_A)

#df_banco_A = df_banco_A.merge(df_banco_B, left_on="ID", right_on="RUT", suffixes=("_bancoA", "_bancoB"))
#print(df_banco_A)

#df_banco_A = df_banco_A.merge(df_banco_B, left_on="ID", right_on="RUT", suffixes=("_bancoA", "_bancoB"), how="left")
#print(df_banco_A)

df_banco_A = df_banco_A.merge(df_banco_B, left_on="ID", right_on="RUT", suffixes=("_bancoA", "_bancoB"), how="outer")
print(df_banco_A)
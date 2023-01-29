import pandas as pd

#1
df_pacientes = pd.read_csv(
    "C:\\Users\\mlevi\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 3\\datos_pacientes.csv",
    encoding="utf-8",
    sep=";"
)
lista = []
for index,row in df_pacientes.iterrows():
    lista.append(row["Monto_Deuda"] * 700)

print(lista[0:10])

#2
print(df_pacientes["Nombre"].str[0:10])

#3
df_pacientes["Nombre"] = df_pacientes["Nombre"].str.upper()
print(df_pacientes["Nombre"])

#4
print(df_pacientes.loc[df_pacientes["Nombre"].str.contains("Ñ")])

#5
df_pacientes2 = pd.read_csv(
    "C:\\Users\\mlevi\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 3\\datos_pacientes2.csv",
    encoding="utf-8",
    sep=";"
)

#6
df_pacientes2 = df_pacientes2.drop(df_pacientes2.loc[df_pacientes2["RUT"].str.contains("XXXX")].index)
df_pacientes2 = df_pacientes2.drop(df_pacientes2.loc[df_pacientes2["Nombre"].str.contains("XXXX")].index)
print(df_pacientes2)

#7
df_pacientes2["Nombre"] = df_pacientes2["Nombre"].str.replace("-", " ")
print(df_pacientes2["Nombre"])

#8
df_pacientes2["Fecha_Nacimiento"] = df_pacientes2["Fecha_Nacimiento"].str.replace("_/", "/")
print(df_pacientes2["Fecha_Nacimiento"])

#9
df_pacientes2["Nombre"] = df_pacientes2["Nombre"].str.upper()
df_pacientes = df_pacientes.append(df_pacientes2)
print(df_pacientes)

#10
df_pacientes = df_pacientes.set_index("RUT")
print(df_pacientes)

#11
df_nombres = df_pacientes["Nombre"].str.split(" ",expand=True)
df_nombres.columns = ["primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido"]
df_pacientes = df_pacientes.join(df_nombres)
print(df_pacientes)

#12
df_nacionalidad = pd.read_csv(
    "C:\\Users\\mlevi\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 3\\nacionalidad.csv",
    encoding="utf-8", sep=";")
df_pacientes = df_pacientes.merge(df_nacionalidad, left_index=True, right_on="RUT", how="left")
df_pacientes = df_pacientes.set_index("RUT")
print(df_pacientes)





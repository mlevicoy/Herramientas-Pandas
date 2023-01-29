import pandas as pd

df_clientes = pd.read_csv(
    "C:\\Users\\mlevi\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Modulo 1\\clientes.csv", 
    encoding="latin-1", sep=";")

print(df_clientes.dtypes)

for index,row in df_clientes.iterrows():
    print(row["RUT"])

print(df_clientes["RUT"].str.len())

print(df_clientes["RUT"].str[11])

print(df_clientes["NOMBRE"].str[6:12])

print(df_clientes["RUT"].str.replace(".",""))

print(df_clientes["TIPO_CLIENTE"].str.contains("C"))

df_fecha_nac = df_clientes["FECHA_NAC"].str.split("/",expand=True)
df_fecha_nac.columns = ["Dia", "Mes", "Año"]
print(df_fecha_nac)

df_clientes = df_clientes.join(df_fecha_nac)
print(df_clientes)




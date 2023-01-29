import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Agregamos la columna NACIONALIDAD y la completamos con CHILE 
df["NACIONALIDAD"] = "CHILE"
# Guardamos los cambios en un archivo nuevo .CSV
df.to_csv("clientes_modificado.csv",sep=";",index=False)
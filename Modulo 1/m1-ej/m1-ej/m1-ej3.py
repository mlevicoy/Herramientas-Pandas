# Importamos la librería Pandas y la renombramos
import pandas as pd
# Leemos el archivo .CSV y generamos un Data Frame
# encoding para que reconozca los carácteres latino y 
# el separador por punto y coma
df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Mostramos el Data Frame
print(df)
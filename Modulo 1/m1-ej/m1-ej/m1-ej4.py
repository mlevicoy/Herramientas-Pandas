# Importamos la librería Pandas y la renombramos
import pandas as pd
# Generamos el Data Frame a través del archivo .CSV
df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Mostramos los tipos de datos de cada columna
print(df.dtypes)
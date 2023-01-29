import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Mostramos las estadísticas descriptivas, que son:
# cuenta, promedio, desviación estándar, mínimo, cuartiles,
# máximo de las columnas numéricas.
print(df.describe())
import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Mostramos todas las filas que tengan su columna MONTO
# menor a 100.000
print(df.loc[df['MONTO'] < 100000])
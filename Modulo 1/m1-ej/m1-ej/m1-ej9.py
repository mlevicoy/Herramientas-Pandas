import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Muestra todas las filas cuyo TIPO CLIENTE sea "A"
print(df.loc[df['TIPO_CLIENTE'] == "A"])
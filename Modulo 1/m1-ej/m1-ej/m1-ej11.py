import pandas as pd

df = pd.read_csv("clientes.csv",encoding="latin-1",sep=";")
# Mostramos las filas cuya columna PUNTAJE CREDITICIO sea 
# menor o igual a 8.0
df_final = df.loc[df['PUNTAJE_CREDITICIO'] <= 8.0]

print(df_final)
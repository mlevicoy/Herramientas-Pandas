# Importamos la libreria panda y la renombramos
import pandas as pd
# Creamos una lista de listas
data = [["Felipe",24,"Masculino",4.5],["Andrea",21,"Femenino",7.0],
		["Tomás",22,"Masculino",6.1],["Roberto",20,"Masculino",5.5]]
# Creamos un Data Frame a partir de la lista de listas
df = pd.DataFrame(data)
# Mostramos el Data Frame
print(df)
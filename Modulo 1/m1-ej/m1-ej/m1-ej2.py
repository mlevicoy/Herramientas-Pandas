# Importamos la librería Pandas y la renombramos
import pandas as pd
# Creamos una lista de listas
data = [["Felipe",24,"Masculino",4.5],["Andrea",21,"Femenino",7.0],
		["Tomás",22,"Masculino",6.1],["Roberto",20,"Masculino",5.5]]
# Creamos un Data Frame con la lista de listas, y agregamos las columnas
# para que no aparezcan números
df = pd.DataFrame(data,columns = ["Nombre","Edad","Género","Calificación"])
# Mostramos el Data Frame
print(df)
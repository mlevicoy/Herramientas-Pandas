# Archivo escrito con vscode

# importamos las librerias
import pandas as pd
import numpy as np

# PROCESAMIENTO Y LIMPIEZA  

# 1)
# cargar el archivo "detalle_boletas.csv" en un Data Frame de nombre "detalle_boletas"
detalle_boletas = pd.read_csv(
    #"C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Final\\detalle_boletas.csv",
    "detalle_boletas.csv",
    encoding="utf-8",
    sep=","
)

# 2)
# eliminar columna "Precio_prod"
del detalle_boletas["Precio_prod"]

# crear columna "Pais_Venta" con valores "Chile"
detalle_boletas["Pais_Venta"] = "Chile"

# cambia el nombre de la columna "NXXX" por "Num Boleta"
detalle_boletas = detalle_boletas.rename(columns={"NXXX":"Num Boleta"})

# 3)
# elimina filas del Data Frame "detalle_boletas" donde la columna "ID" tenga los valores
# "4XXXXX" y la columna "Num Boletas" tenga valores "55417XXXXXXX"
detalle_boletas = detalle_boletas.drop(detalle_boletas.loc[(detalle_boletas["ID"] == "4XXXXX") | (detalle_boletas["Num Boleta"] == "55417XXXXXXX")].index)

# eliminar caracteres extras en la columna "Fecha"
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("!/{","/", regex=False)
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("-/.","/", regex=False)
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].str.replace("_/","/", regex=False)

# 4)
# calcular e imprimir estadísticos descriptivos de la columna cantidad para todos los productos del dataframe
estadisticos_descriptivos = detalle_boletas.pivot_table(index="ID", values="Cantidad", aggfunc={np.mean, np.std, np.min, np.max})
print(estadisticos_descriptivos)

# 5)
# separar la columna "Fecha" en tres columnas "Anho", "Mes" y "Dia"
fechas_boletas = detalle_boletas["Fecha"].str.split("/", expand=True)
fechas_boletas.columns = ["Anho", "Mes", "Dia"]

# agregar estas columnas al Data Frame "detalle boletas"
detalle_boletas = detalle_boletas.join(fechas_boletas)

# eliminar la columna "Fecha" después de agregar las columnas "Anho", "Mes" y "Dia"
del detalle_boletas["Fecha"]

# EXTRACCIÓN DE INFORMACIÓN DE LOS DATOS

# 6)
# carga "Lista productos.csv" en un Data Frame de nombre "lista_productos"
lista_productos = pd.read_csv(
    #"C:\\Users\\Usuario\\OneDrive - Bogado Ingenieros Consultores SpA\\MIRESPALDO\\Cursos\\Python\\Final\\Lista productos.csv",
    "Lista productos.csv",
    encoding="utf-8",
    sep=","
)

# 7)
# unir el Data Frame "lista_productos" a "detalle_boletas" en base a la información de la columna "ID",
# según lo especificado en las instrucciones. Asignar el Data Frame resultante a un nuevo Data Frame llamado
# "detalle_boletas2"
print("--- Tipos de datos - detalle_boleta ---")
print(detalle_boletas.dtypes)
print("--- Tipos de datos - lista_productos ---")
print(lista_productos.dtypes)
lista_productos["ID"] = lista_productos["ID"].astype(str)
detalle_boletas2 = detalle_boletas.merge(lista_productos, left_on="ID", right_on="ID", how="left")
detalle_boletas2 = detalle_boletas2.set_index("ID")

# imprimir detalle_boletas2
print(detalle_boletas2)

# 8)
# crear columna "Ingreso total" como la multiplicación de la columna "Precio Unitario" y "Cantidad" en el
# Data Frame detalle_boleta2
detalle_boletas2["Ingreso total"] = (detalle_boletas2["Precio Unitario"] * detalle_boletas2["Cantidad"])

# imprimir el Data Frame detalle_boletas2 con la nueva columna "Ingreso Total"
print(detalle_boletas2)

# 9)
# calcular e imprimir estadísticos descriptivos de la columna "Ingreso total" para todos los productos
# del Data Frame detalle_boletas2
estadisticos_descriptivos2 = detalle_boletas2.pivot_table(index="ID", values="Ingreso total", aggfunc={np.mean, np.std, np.min, np.max, np.sum})
print(estadisticos_descriptivos2)
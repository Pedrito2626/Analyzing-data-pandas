import pandas as pd

df = pd.read_excel("C:\\Users\AZUser\Downloads\BD_LISTA.xlsx")
print(df)  # Imprime el DataFrame completo
df.shape  # Muestra la forma del DataFrame (número de filas y columnas)
df.columns
df.index  # Muestra los índices del DataFrame
# df["Nombre"]  # Accede a la columna "Nombre"
# df["Nombre"]["trabajador1"]  # Accede al segundo elemento de la columna "Nombre"
# df.iloc[0]  # Accede a la primera fila del DataFrame
# df["Edad"].mean()  # Calcula la media de la columna "Edad"
df.describe()  # Muestra la descripción estadística del DataFrame
# count: número de elementos no nulos
# mean: media de los valores numéricos
# std: desviación estándar
# min: valor mínimo
# 25%: primer cuartil
# 50%: mediana
# 75%: tercer cuartil
# max: valor máximo
df.info()  # Muestra información general del DataFrame
len(pd.unique(df["NOMBRE"]))  # Cuenta el número de valores únicos en la columna "Nombre"
df.duplicated()  # Muestra si hay filas duplicadas
df.groupby("FRUTA PREFERIDA").size()  # Agrupa por la columna "Semestre" y cuenta el número de ocurrencias
df.groupby("NIVEL PROGR").size() 
# Agrupa por la columna "Semestre" y cuenta el número de ocurrencias, reseteando el índice
df.groupby
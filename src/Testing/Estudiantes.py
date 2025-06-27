import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
Actividad en clase:
#TODO 1 - Realizar los hallazgos del anterior ejercicio
#TODO 2 - En la base de datos de estudiantes del salon, añadir una columna nueva donde se visualice el sexo, edad, barrio y municipio donde reside
#TODO 3 - Realizar graficas para identificar visualmente si existe relacion entre el municipio en que reside y el sexo
#TODO 4 - Realizar graficas para identificar visualmente si existe relacion entre el programa y la edad
#TODO 5 - Realizar grafica para visualizar si existe relacion entre la fruta preferida, la edad y el sexo
#TODO 6 - Realizar histograma de las edades en funcion del sexo
"""

df = pd.read_excel("C:\\Users\AZUser\Downloads\BD_LISTA.xlsx")
df.shape  # Muestra la forma del DataFrame (número de filas y columnas)
df.columns
df.index  # Muestra los índices del DataFrame
df.replace("medellin", "Medellin", inplace=True)
df.replace("envigado", "Envigado", inplace=True)
df.replace("caldas", "Caldas", inplace=True)
df.replace("itagui", "Itagui", inplace=True)
df.replace("girardota", "Girardota", inplace=True)
df.isnull().sum()  # Muestra el número de valores nulos en cada columna

df = df.dropna()  # Elimina filas con valores nulos
df["EDAD"] = df["EDAD"].astype(int)  # Convierte la columna EDAD a tipo entero
sns.catplot(x="MUNICIPIO", hue="SEXO", data=df, kind="count")
sns.catplot(x="ESTUDIO", hue="SEXO", data=df, kind="count")
sns.catplot(x="FRUTA PREFERIDA", y="EDAD", hue="SEXO", data=df, kind="violin", height=6, aspect=2)
sns.histplot(data=df, x="EDAD", hue="SEXO", multiple="stack", kde=True, palette="Set1", bins="auto")

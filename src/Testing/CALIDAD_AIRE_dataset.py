# abc

# ! Ejercicio de Calidad del Aire

# TODO Descargar base de datos de calidad del aire
# TODO Subir a pandas el archivo csv
# TODO Visualizar dimensionalidad del archivo
# TODO Visualizar columnas
# TODO Realizar análisis estadístico descriptivo
# TODO Identificar ciudad con mayor cantidad de cada uno de los contaminantes
# TODO Identificar ciudad con menor cantidad de cada uno de los contaminantes
# TODO calcular promedio de cada uno de los contaminantes por ciudad


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

df = pd.read_csv("C:\\Users\AZUser\Downloads\Air_Quality.csv")
df
print(f"Dimensiones del dataset:\n {df.shape}")
print(f"Nombre de las columnas: \n{df.columns}")
print(f"Análisis estadístico descriptivo:\n {df.describe()}")

# ? Identificar ciudad con mayor y menor cantidad de cada contaminante

for contaminant in df.columns[2:]:
    max_city = df.loc[  # * Busca el índice del valor máximo del contaminante y luego con loc usa el índice para obtener la ciudad
        df[contaminant].idxmax(), "City"
    ]
    min_city = df.loc[  # * Busca el índice del valor mínimo del contaminante y luego con loc usa el índice para obtener la ciudad
        df[contaminant].idxmin(), "City"
    ]
    df_mean = df.groupby(
        ["City"]
    )[  # * Agrupa por ciudad y calcula el promedio del contaminante
        contaminant
    ].mean()

    print(f"Ciudad con mayor {contaminant}: {max_city} ({df[contaminant].max()})")
    print(f"Ciudad con menor {contaminant}: {min_city} ({df[contaminant].min()})")
    print(f"Promedio de {contaminant} por ciudad:\n{df_mean}")

# ? Gráfica de histograma del contaminante CO
sns.histplot(data=df, x=df["CO"])
plt.title("Histograma de CO")
plt.xlabel("CO")
plt.ylabel("Frecuencia")
plt.show()  # * muestra el histograma y quita etiquetas de los ejes

# ? Gráfica de boxplot del contaminante CO por ciudad
sns.boxplot(
    data=df,
    x=df["City"],  # * categoria para agrupar
    y=df["CO"],  # * campo a evaluar
)
plt.title("Boxplot de CO por ciudad")
plt.show()  # * muestra el boxplot y quita etiquetas de los ejes

# ? Gráfica de histograma, pero apilada
sns.histplot(
    data=df,
    x=df["CO"],
    hue="City",  # * apila por ciudad
    multiple="stack",  # * apila los histogramas
)
plt.title("Histograma de CO por ciudad apilado")
plt.show()  # * muestra el histograma y quita etiquetas de los ejes

# ? Gráfica de histograma de PM2.5 por ciudad apilada
sns.histplot(
    data=df,
    x=df["PM2.5"],
    multiple="stack",
    hue="City",
    kde=True,  # * añade una línea de densidad, permite visualizar la tendencia
)
plt.title("Histograma de PM2.5 por ciudad apilado")
plt.show()  # * muestra el histograma y quita etiquetas de los ejes

# ? Transformar datos: fecha a datetime
df["Date"] = pd.to_datetime(df["Date"])

#? Extraer el número del mes y el nombre del mes de la fecha
df["Mes_num"] = df["Date"].dt.month  # * extra el número del mes

df["Mes_nombre"] = df["Date"].dt.month.apply( #* Usa el número del mes para extraer el nombre del mes
    lambda x: calendar.month_name[x]
)
# for contaminant in df.columns[2:-2]:
#     print(
#         f"Promedio de {contaminant} por mes:\n{df.groupby(['Mes_nombre'])[contaminant].mean()}"
#     )
#? Crear un nuevo dataframe con el promedio de cada contaminante por mes
contaminantes = df.columns[2:-2]
promedio_ordenado = {} #* Creamos un diccionario vacío para guardar los promedios ordenados por contaminante

for i in contaminantes:
    #* Calculamos el promedio de cada contaminante agrupando el DataFrame 'df' por número y nombre de mes, 
    #* permite que se ordenen cronológicamente los meses
    valor_promedio = df.groupby(["Mes_num","Mes_nombre"])[i].mean()
    #* Guardamos el resultado en el diccionario usando el nombre del contaminante como clave
    promedio_ordenado[i] = valor_promedio

#* Convertimos el diccionario de promedios en un DataFrame para facilitar su análisis y visualización
promedio_df = pd.DataFrame(promedio_ordenado)

#? Graficar tendencia de promedio de CO a lo largo de los meses
plt.figure(figsize=(12, 6)) #* Ajusta el tamaño de la figura
plt.plot(
    #? get_level_values sirve para obtener los valores de un nivel específico, sólo se usa cuando el índice es jerárquico
    promedio_df.index.get_level_values("Mes_num"), #* Valores del eje x (número de mes)
    promedio_df["CO"].values, #* Valores del eje y (promedio de CO)
    marker="o", #* Marca los puntos con círculos
    color="blue", #* Color de la línea
    linestyle="-") #* Estilo de la línea
plt.title("Tendencia de CO a lo largo de los meses")
plt.xlabel("Mes")
plt.ylabel("Promedio de CO")
plt.show()  # * muestra la gráfica y quita etiquetas de los ejes

""" 
#TODO
- Cuales son los meses con mayor promedio de contaminacion? como es su desviacion estandar?
- Cuales son los meses con menor promedio de contaminacion? como es su desviacion estandar?
- Hay alguna similitud o patron entre los de mayor y menor a lo largo del año?
- Las ciudades con picos más altos en contaminantes, coinciden con los mayores promedios?
- Las ciudades con picos más bajos en contaminantes, coinciden con los menores promedios?
- Plantear posibles causas de mayores picos
""" 
# Calcular la suma de los promedios de contaminantes por mes
promedio_df["Promedio_contaminantes"] = promedio_df.mean(axis=1)

# Calcular la desviación estándar de la columna promedio_contaminantes por mes
promedio_df["Desviacion_std"] = promedio_df["Promedio_contaminantes"].std()

# Ordenar de mayor a menor según la suma de promedios
resultados = promedio_df.sort_values("Promedio_contaminantes", ascending=False)[["Promedio_contaminantes", "Desviacion_std"]]

print("Meses con mayor promedio de contaminación (suma de promedios de contaminantes) y su desviación estándar:")
print(resultados)
"""
Se puede concluir según los datos que lso meses con más contaminación son los tres ultimos
Esto, realmente, se debe a que son estos los únicos que tienen datos en CO2, por lo que dispara sus resultados
"""
plt.figure(figsize=(12, 6))
# Graficar la suma de promedios de contaminantes (línea roja)
plt.plot(
    promedio_df.index.get_level_values("Mes_num"),
    promedio_df["Promedio_contaminantes"].values,
    marker="o",
    color="red",
    linestyle="-",
    label="Promedio de contaminantes"
)
plt.title("Tendencia de los promedios de contaminantes a lo largo de los meses")
plt.xlabel("Mes")
plt.ylabel("Promedio de contaminantes")
plt.show()  # * muestra la gráfica y quita etiquetas de los ejes
# Graficar el promedio de cada contaminante por ciudad (líneas de colores)
for ciudad in df["City"].unique():
    # Agrupa por mes y ciudad, calcula el promedio de todos los contaminantes
    promedio_ciudad = df[df["City"] == ciudad].groupby(["Mes_num"])[["CO", "NO2", "PM2.5", "SO2", "O3", "CO2"]].mean().sum(axis=1)
    plt.plot(
        promedio_ciudad.index,
        promedio_ciudad.values,
        marker="o",
        linestyle="--",
        label=f"{ciudad}"
    )
plt.title("Tendencia de los promedios de contaminantes a lo largo de los meses por ciudad")
plt.xlabel("Mes")
plt.ylabel("Promedios de contaminantes")
plt.legend(title="Ciudad", bbox_to_anchor=(1.05, 1), loc='upper left')

"""
En sí no se ve una similitud entre los meses con mayor y menor promedio de contaminación.
Es díficil establecer un patrón claro cuando los de menores promedios y además el resto, no tienen datos de CO2.
Sí
Sí
Al no haber datos de CO2, los datos y las comparaciones son limitados. No veridicos.
"""
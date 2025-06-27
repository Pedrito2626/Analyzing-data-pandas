import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar archivos
train = pd.read_csv("C:\\Users\\AZUser\\Downloads\\train.csv")
test = pd.read_csv("C:\\Users\\AZUser\\Downloads\\test.csv")
train.head()
test.head()
train.shape  # Muestra la forma del DataFrame (número de filas y columnas)
test.shape  # Muestra la forma del DataFrame (número de filas y columnas)
train.dtypes  # Muestra los tipos de datos de cada columna
test.dtypes  # Muestra los tipos de datos de cada columna
train.isnull().sum()  # Muestra el número de valores nulos en cada columna
test.isnull().sum()  # Muestra el número de valores nulos en cada columna
train.describe()  # Muestra estadísticas descriptivas del DataFrame
test.describe()  # Muestra estadísticas descriptivas del DataFrame
train.columns
test.columns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = sm.datasets.co2.load_pandas().data
fig, ax = plt.subplots(
    figsize=(13, 11)
)  # ? Ajusta la figura y la información de lso ejes
ax.plot(data["co2"])
ax.set_title("Concentración de CO2 en la atmósfera (1958-2001)")
ax.set_xlabel("Año")
ax.set_ylabel("Concentración de CO2 (PPMW)")
data.isnull().sum()

data = data.interpolate()  # ? Interpolación de los valores nulos

#! Estadística multivariada
"""
Matriz de correlación: es una tabla que muestra la relación entre varias variables, indica fuerza y dirección de la relación.
    Correlación de Pearson: mide la relación lineal entre dos variables.
    Indica la relación que tienen dos variables, si son positivas o negativas, y la fuerza de esa relación.
    La correlación de Pearson es un valor entre -1 y 1, donde:
    Tiende a -1: indica una relación negativa perfecta, si una variable aumenta, la otra disminuye,
    Tiende a 0: indica que no hay relación lineal,
    Tiende a 1: indica una relación positiva perfecta, si una variable aumenta, la otra también aumenta.
"""
# ? Ejemplo de matriz de correlación negativa
x = np.array([10, 12, 15, 18, 21])
y = np.array([100, 83, 67, 56, 50])
corr_matrix = np.corrcoef(x, y)  # ? Matriz de correlación
print("Matriz de correlación:\n", corr_matrix)
# ? Ejemplo de matriz de correlación positiva
x2 = np.array([10, 12, 15, 18, 21])
y2 = np.array([12, 9, 10, 11, 17])
corr_matrix2 = np.corrcoef(x2, y2)  # ? Matriz de correlación
print("Matriz de correlación:\n", corr_matrix2)

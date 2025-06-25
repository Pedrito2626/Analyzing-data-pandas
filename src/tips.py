import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dfTips = sns.load_dataset("tips")
dfTips.head()
dfTips.describe()
dfTips.info()
dfTips.isnull().sum()
dfTips.columns
dfTips.shape
dfTips.dtypes
#! Datos interesantes del dataset, se pueden usar para análisis estadísticos
dfTips["total_bill"].max()
dfTips["total_bill"].min()
dfTips["total_bill"].mean()
dfTips["total_bill"].median()
dfTips["total_bill"].std()

dfTips["tip"].max()
dfTips["tip"].min()
dfTips["tip"].mean()
dfTips["tip"].median()
dfTips["tip"].std()

dfTips["size"].max()
dfTips["size"].min()
dfTips["size"].mean()

dfTips["smoker"].value_counts() #? Cuenta el número de clientes fumadores y no fumadores
dfTips["sex"].value_counts() #? Cuenta el número de clientes masculinos y femeninos
dfTips["day"].value_counts() #? Cuenta el número de clientes por día
dfTips["time"].value_counts() #? Cuenta el número de clientes por hora (almuerzo o cena)

#! 1. Heatmap de correlación entre variables numéricas
#? Visualiza la relación entre las variables numéricas del dataset
numtips = dfTips.select_dtypes(include=[np.number])
sns.heatmap(numtips.corr(), annot=True, cmap='coolwarm')

sns.catplot(x="day", y="total_bill", data=dfTips)
sns.catplot(x="day", y="total_bill", data=dfTips, kind="swarm", hue="sex")

#! 2. Histograma de la cuenta total
#? Muestra la distribución de los montos de las cuentas
sns.histplot(dfTips["total_bill"], bins=20, kde=True)
plt.title("Distribución de la cuenta total")
plt.xlabel("Cuenta total")
plt.ylabel("Frecuencia")
plt.show()

#! 3. Gráfico de dispersión entre cuenta total y propina
#? Analiza la relación entre el monto de la cuenta y la propina
sns.scatterplot(x="total_bill", y="tip", data=dfTips, hue="sex")
plt.title("Relación entre cuenta total y propina")
plt.xlabel("Cuenta total")
plt.ylabel("Propina")
plt.legend(title="Sexo")
plt.show()

#! 4. Gráfico de barras del total de cuentas por día y por sexo
#? Compara el monto promedio de las cuentas según el día y el sexo del cliente
sns.barplot(x="day", y="total_bill", hue="sex", data=dfTips, ci=None)
plt.title("Cuenta total promedio por día y sexo")
plt.xlabel("Día")
plt.ylabel("Cuenta total promedio")
plt.show()
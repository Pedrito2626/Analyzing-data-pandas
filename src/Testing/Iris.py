import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

data = load_iris()
iris_df = pd.DataFrame(data=data.data, columns=data.feature_names)
iris_df.describe()
iris_df.corr()
iris_df.info()
iris_df.isnull().sum()
iris_df.columns
iris_df.head()
iris_df.describe()


#! Mapa de calor de la matriz de correlación, muestra valores númericos y la relación entre las variables
plt.figure(figsize=(14, 6))
heatmap = sns.heatmap(iris_df.corr(), annot=True, vmin=-1, vmax=1)
heatmap.set_title("Matriz de Correlación", fontdict={"fontsize": 12})

#! Otro mapa de calor, pero sólo se muestra el triángulo superior de la matriz de correlación, asi se evitan duplicados visuales
plt.figure(figsize=(16, 6))
mask = np.triu(np.ones_like(iris_df.corr(), dtype=bool))
heatmap = sns.heatmap(iris_df.corr(), annot=True, mask=mask, vmin=-1, vmax=1)
heatmap.set_title("Triángulo de correlación", fontdict={"fontsize": 18})

iris_df["target"] = ( # ? Se crea una columna "Target", que indica la especie de cada flor, 0, 1 o 2
    data.target
)  

#! Gráfico de dispersión de las características del Iris, coloreado por la especie
sns.pairplot(iris_df, hue="target", palette="dark", height=2.5)
plt.show()

#! El mismo de arriba pero sólo se muestra el triángulo superior
sns.pairplot(iris_df, hue="target", palette="tab10", height=2.5, corner=True)
plt.show()

#! Para cada característica, se crea un gráfico de violín que muestra la distribución de valores para cada especie.
features = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="target", y=feature, data=iris_df, palette="tab10", hue="target")
    plt.title(f"Violin plot de {feature}")
    plt.show()

#! Se reorganizan los datos con melt para tener una columna de características y otra de valores.
#! Se crea un gráfico de violín combinado para comparar todas las características y especies en un solo gráfico.
dfMelted = iris_df.melt(
    id_vars="target", value_vars=features, var_name="feature", value_name="value"
)
plt.figure(figsize=(12, 8))
sns.violinplot(
    x="feature", y="value", hue="target", data=dfMelted, split=True, palette="tab10"
)
plt.title("Violin plot de las características del Iris")
plt.xlabel("Características")
plt.ylabel("Valor (cm)")
plt.show()

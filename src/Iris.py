import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.datasets import load_iris 

data = load_iris()
iris_df = pd.DataFrame(data = data.data, columns=data.feature_names)
iris_df.describe()
iris_df.corr()
plt.figure(figsize=(14, 6))
heatmap = sns.heatmap(iris_df.corr(), annot=True, vmin=-1, vmax=1)
heatmap.set_title('Matriz de Correlación', fontdict={'fontsize':12})
plt.figure(figsize=(16, 6))
mask = np.triu(np.ones_like(iris_df.corr(), dtype=bool))
heatmap = sns.heatmap(iris_df.corr(), annot=True, mask=mask, vmin=-1, vmax=1)
heatmap.set_title('Triángulo de correlación', fontdict={'fontsize':18})

iris_df['target'] = data.target
sns.pairplot(iris_df, hue='target', palette='dark', height=2.5)
plt.show()
sns.pairplot(iris_df, hue='target', palette='tab10', height=2.5, corner=True)
plt.show()

features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='target', y=feature, data=iris_df, palette='tab10', hue='target')
    plt.title(f'Violin plot de {feature}')
    plt.show()  

dfMelted = iris_df.melt(id_vars='target', value_vars= features, var_name='feature', value_name='value')
plt.figure(figsize=(12, 8))
sns.violinplot(x='feature', y='value', hue='target', data=dfMelted, split=True, palette='tab10')
plt.title('Violin plot de las características del Iris')
plt.xlabel('Características')
plt.ylabel('Valor (cm)')
plt.show()
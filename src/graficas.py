import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#! Usando la funcion plt.plot se genera una figura y un conjunto de ejes de forma implícita

# ? sns.set(): sirve para cambiar el estilo de las graficas y que todas tengan un mismo estilo
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # ? Genera 100 puntos entre -2π y 2π
plt.plot(x, np.sin(x), "bo-.", label="Seno")  # ? Traza la función seno
plt.plot(x, np.cos(x), "ro-", label="Coseno")  # ? Traza la función coseno
plt.title("Funciones Seno y Coseno")  # ? Titulo de la gráfica
plt.xlabel("x")  # ? Etiqueta del eje x
plt.ylabel("y")  # ? Etiqueta del eje y
plt.legend()  # ? Muestra la leyenda de las funciones
plt.grid()  # ? Muestra la cuadrícula en la gráfica
plt.savefig("seno_coseno.png")  # ? Guarda la figura en un archivo PNG
plt.show()

#! Estilo POO: Se referencia la figura y los ejes con las variables 'fig' y 'ax' respectivamente.
# ? Usar plr.figure y plt.axes nos devuelven  una referencia de la figura y de los ejes utilizados
fig = plt.figure()
ax = plt.axes()

# ? Una vez que tenemos la figura y los ejes, podemos graficar ejecutando el método plot sobre ax
y = np.sin(x)
ax.plot(x, y, label="Seno", color="blue")

plt.plot(x, y, color="blue", linestyle="-.", marker="o", markersize=5, label="Seno")

plt.plot(x, y, color="g", linestyle="-.", marker="o")

#! Ajuste de los ejes
# ? plt.axis([xmin, xmax, ymin, ymax]): Valores de la gráfica, para definir el rango de los ejes
plt.plot(
    x, y, "gs-."
)  # ? 'gs-.' es un atajo para definir el color, el marcador y el estilo de la línea en un solo string
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Gráfica del Seno")
plt.axis(
    [-2 * np.pi - 0.5, 2 * np.pi + 0.5, -1.5, 1.5]
)  # ? Define el rango de los ejes x e y
plt.show()  # ? Muestra la gráfica

#! Otro ejemplo
plt.plot(x, y, "co:")
plt.xlabel(
    "$x$"
)  # ? lo que esté dentro de '$...$' se mostrará en estilo matemático, como las ecuaciones de Word
plt.ylabel("$\sin(x)$")
plt.title("Gráfica del Seno")
plt.axis("tight")  # ? Ajusta los ejes para que se ajusten al rango de los datos
plt.show()

#! Legenda
plt.plot(x, y, "r^-", label="$sin(x)$")
plt.xlabel("$x$")
plt.ylabel("$\sin(x)$")
plt.title("Gráfica del Seno")
plt.legend(loc="best")
plt.axis("tight")
plt.show()

#! metodo ax.set() para establecer todas las propiedades de la gráfica
fig, ax = plt.subplots()  # ? Crea una figura y un conjunto de ejes
ax.plot(x, y, "g*:", label="$\sin(x)$")
ax.set(xlabel="$x$", ylabel="$\sin(x)$", title="Gráfica del Seno")
ax.axis("tight")
ax.legend(loc="upper right")
plt.show()

#! Para crear múltiples gráficos en una sola figura, se puede usar plt.subplots()
#! Se usa ax.plot() reiteradamente para tener dos gráficos en la misma figura
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, "g*:", label="$\sin(x)$")
ax.plot(x, np.cos(x), "bo--", label="$\cos(x)$")
ax.set(xlabel="$x$", ylabel="$y(x)$", title="Gráfica del Seno y Coseno")
ax.axis("tight")
ax.legend()
ax.grid(True)  # ? Añade una cuadrícula a la gráfica
plt.show()

fig, ax = plt.subplots(
    2,
    2,
    constrained_layout=True,  # ? constrained_layout sirve para ajustar automáticamente el espacio entre los subgráficos
    figsize=(10, 6),
)
ax[0, 0].plot(x, y)
ax[0, 1].plot(x, np.cos(x))
ax[1, 0].plot(x, np.tan(x))
ax[1, 1].plot(x, np.arctan(x))

ax[0, 0].set(title="Seno", xlabel="$x$", ylabel="y")
ax[0, 1].set(title="Coseno", xlabel="$x$", ylabel="y")
ax[1, 0].set(title="Tangente", xlabel="$x$", ylabel="y")
ax[1, 1].set(title="Cotangente", xlabel="$x$", ylabel="y")
ax[0, 0].grid(True)
ax[0, 1].grid(True)
ax[1, 0].grid(True)
ax[1, 1].grid(True)
plt.show()

#! Ejemplo práctico
nba = pd.read_csv(
    "https://raw.githubusercontent.com/tomasate/Datos_Clases/main/Datos_1/nba.csv",
    index_col="Unnamed: 0",
)
nba["College"] = nba["College"].fillna("No College")
nba["Salary"] = nba["Salary"].fillna(0).astype(int)
nba = nba.drop(457)  # ? elimina la fila
nba.describe()  # ? Muestra estadísticas descriptivas de las columnas numéricas
Top5equiposMasSalarios = (
    nba.groupby("Team")["Salary"].sum().sort_values(ascending=False).head(5)
)
# todo: Separar la variable age en tres grupos y crear una columan llamada "Age-Group", con esta información:
# todo: Mostrar un gráfico de barras con el número de los jugadores por grupo de edad, con hue en la posición en la que juegan
nba["Age-Group"] = pd.cut(
    nba["Age"], bins=[0, 25, 35, 40], labels=["<25", "25-35", ">35"]
)
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(
    data=nba, x="Age-Group", hue="Position", palette="pastel", edgecolor="black", ax=ax
)
ax.set_title("Número de jugadores por grupo de edad y posición")
ax.set_xlabel("Grupo de Edad")
ax.set_ylabel("Número de Jugadores")

fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
sns.boxplot(
    data=nba, x="Position", y="Salary", palette="pastel", ax=axes[0], hue="Position"
)
axes[0].set_title("Salarios por Posición")
axes[0].set_xlabel("Posición")
axes[0].set_ylabel("Salario")

sns.boxplot(
    data=nba, x="Age-Group", y="Salary", palette="pastel", ax=axes[1], hue="Age-Group"
)
axes[1].set_title("Salarios por Grupo de Edad")
axes[1].set_xlabel("Grupo de Edad")
axes[1].set_ylabel("")

plt.tight_layout()
plt.show()
# ? Construir una tabla que muestre el salario promedio por equipo y por posición para los cinco equipos con mayor salario. Visualizar los resultados en un mapa de calor.
avg_salary = nba.groupby(["Team", "Position"])["Salary"].mean().unstack()
avg_salary.fillna(0, inplace=True)  # ? Rellena los valores NaN con 0
fig, ax = plt.subplots(figsize=(12, 8))

sns.heatmap(avg_salary, annot=True, fmt=".0f", cmap="YlGnBu", ax=ax)
ax.set_title("Salario Promedio por Equipo y Posición")
ax.set_xlabel("Posición")
ax.set_ylabel("Equipo")
plt.show()

"""
# Problema: Análisis de Rendimiento Comercial

## Descripción del Problema:

Supongamos que trabajamos en una empresa que se dedica a la venta de productos electrónicos, y nos enfrentamos al desafío de mejorar el rendimiento de nuestro negocio. Para lograrlo, necesitamos aprovechar al máximo la información contenida en nuestros datos de ventas. Estos datos incluyen información detallada sobre las transacciones de ventas a lo largo de varios años.

El objetivo principal es analizar estos datos para obtener información valiosa que nos permita tomar decisiones informadas y estratégicas. Algunas de las cuestiones clave que queremos abordar incluyen:
+ Tendencias Temporales: ¿Existe alguna estacionalidad en nuestras ventas? ¿Cómo han evolucionado a lo largo de los años?
+ Perfil del Cliente: ¿Quiénes son nuestros clientes? ¿Podemos segmentarlos en grupos con características similares?
+ Rendimiento de Productos: ¿Cuáles son los productos más rentables y cuáles son los menos rentables?
+ Ubicaciones: ¿Dónde se concentran nuestras ventas? ¿Existen diferencias significativas entre regiones o estados?

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


url = "https://raw.githubusercontent.com/ine-rmotr-curriculum/FreeCodeCamp-Pandas-Real-Life-Example/master/data/sales_data.csv"
df = pd.read_csv(url)
df.head()
df.isnull().sum()
df.duplicated().sum()
df.info()
df.describe()

#! Visualización de cantidad de clientes por edad
plt.figure(figsize=(10, 6))
plt.hist(df["Customer_Age"], bins=20, color="skyblue", edgecolor="k")
plt.title("Distribución de la Edad del Cliente")
plt.xlabel("Edad del Cliente")
plt.ylabel("Número de Clientes")
plt.show()

category_sales = (
    df.groupby(["Product_Category", "Sub_Category"])["Revenue"].sum().reset_index()
)
pivot_table = category_sales.pivot(
    index="Product_Category", columns="Sub_Category", values="Revenue"
)

plt.figure(figsize=(8, 5))
plt.imshow(pivot_table, cmap="autumn", aspect="auto")
plt.colorbar(label="Ventas")
plt.title("Ventas por Categoría y Subcategoría de Producto")
plt.xlabel("Subcategoría")
plt.ylabel("Categoría")
plt.xticks(range(len(pivot_table.columns)), labels=pivot_table.columns, rotation=90)
plt.yticks(ticks=np.arange(len(pivot_table.index)), labels=pivot_table.index)

plt.show()

# Opción 3: Gráfica de barras agrupadas más elegante
fig, ax = plt.subplots(figsize=(15, 8))

# Preparar datos para gráfica de barras
pivot_melted = (
    pivot_table.reset_index()
    .melt(id_vars="Product_Category", var_name="Sub_Category", value_name="Revenue")
    .dropna()
)

# Crear gráfica con seaborn
sns.barplot(
    data=pivot_melted,
    x="Sub_Category",
    y="Revenue",
    hue="Product_Category",
    palette="Set2",
    ax=ax,
)

# Personalizar la gráfica
ax.set_title(
    "Rendimiento de Ventas por Categoría y Subcategoría",
    fontsize=18,
    fontweight="bold",
    pad=20,
)
ax.set_xlabel("Subcategoría de Producto", fontsize=14, fontweight="bold")
ax.set_ylabel("Ingresos ($)", fontsize=14, fontweight="bold")

# Formatear eje Y con separadores de miles
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))

# Rotar etiquetas del eje X
plt.xticks(rotation=45, ha="right")

# Personalizar leyenda
ax.legend(
    title="Categoría de Producto",
    title_fontsize=12,
    fontsize=11,
    loc="upper right",
    frameon=True,
    fancybox=True,
    shadow=True,
)

# Agregar grilla sutil
ax.grid(True, alpha=0.3, axis="y")

# Ajustar layout
plt.tight_layout()
plt.show()

df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df["Año"] = df["Date"].dt.year
df["Mes"] = df["Date"].dt.month
ventasMensuales = df.groupby(["Año", "Mes"])["Revenue"].sum()

# Diferentes opciones de marcadores para el gráfico de ventas mensuales
plt.figure(figsize=(14, 8))

# Opción 1: Con círculos
plt.subplot(2, 2, 1)
ventasMensuales.plot(legend=True, marker="o", linestyle="-", color="b", markersize=4)
plt.title("Con marcadores círculo ('o')")
plt.xlabel("Fecha")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Opción 2: Con cuadrados
plt.subplot(2, 2, 2)
ventasMensuales.plot(legend=True, marker="s", linestyle="-", color="red", markersize=4)
plt.title("Con marcadores cuadrado ('s')")
plt.xlabel("Fecha")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Opción 3: Con diamantes
plt.subplot(2, 2, 3)
ventasMensuales.plot(
    legend=True, marker="D", linestyle="-", color="green", markersize=3
)
plt.title("Con marcadores diamante ('D')")
plt.xlabel("Fecha")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Opción 4: Sin marcadores (línea continua)
plt.subplot(2, 2, 4)
ventasMensuales.plot(legend=True, marker="", linestyle="-", color="purple", linewidth=2)
plt.title("Sin marcadores (línea continua)")
plt.xlabel("Fecha")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Gráfico principal mejorado con marcadores
plt.figure(figsize=(14, 6))
ventasMensuales.plot(
    legend=True,
    marker="o",  # Círculos como marcadores
    linestyle="-",  # Línea continua
    color="#2E86AB",  # Color azul profesional
    markersize=5,  # Tamaño del marcador
    markerfacecolor="#A23B72",  # Color de relleno del marcador
    markeredgecolor="white",  # Color del borde del marcador
    markeredgewidth=1,  # Grosor del borde del marcador
    linewidth=2,
)  # Grosor de la línea
plt.title("Ventas Mensuales a lo Largo de los Años", fontsize=16, fontweight="bold")
plt.xlabel("Fecha", fontsize=12)
plt.ylabel("Ventas ($)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Análisis de ventas anuales más profesional
ventasAnuales = df.groupby("Año")["Revenue"].sum()

# Calcular el porcentaje de crecimiento anual de las ventas
crecimiento_anual = ventasAnuales.pct_change() * 100
# Calcular el promedio de ventas anuales
promedio_ventas = ventasAnuales.mean()

# Aplicar un estilo profesional a las gráficas
plt.style.use("seaborn-v0_8-whitegrid")
# Crear una figura con dos subgráficas (barras y línea de crecimiento)
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(14, 12), gridspec_kw={"height_ratios": [3, 1]}
)

# Asignar colores a las barras según si están por encima o debajo del promedio
colors = ["#E74C3C" if x < promedio_ventas else "#2ECC71" for x in ventasAnuales.values]
# Graficar las ventas anuales como barras
bars = ax1.bar(
    ventasAnuales.index,
    ventasAnuales.values,
    color=colors,
    edgecolor="white",
    linewidth=2,
    alpha=0.85,
    width=0.7,
)

# Agregar el valor de cada barra encima de la misma
for i, (year, value) in enumerate(ventasAnuales.items()):
    ax1.text(
        year,
        value + max(ventasAnuales) * 0.01,
        f"${value:,.0f}",
        ha="center",
        va="bottom",
        fontweight="bold",
        fontsize=11,
    )

    # Agregar el porcentaje de crecimiento anual (excepto el primer año)
    if i > 0 and not pd.isna(crecimiento_anual.iloc[i]):
        growth = crecimiento_anual.iloc[i]
        color_growth = "#2ECC71" if growth > 0 else "#E74C3C"
        symbol = "↑" if growth > 0 else "↓"
        ax1.text(
            year,
            value + max(ventasAnuales) * 0.06,
            f"{symbol} {abs(growth):.1f}%",
            ha="center",
            va="bottom",
            fontweight="bold",
            fontsize=10,
            color=color_growth,
        )

# Dibujar una línea horizontal indicando el promedio de ventas
ax1.axhline(
    y=promedio_ventas,
    color="#F39C12",
    linestyle="--",
    linewidth=2,
    alpha=0.8,
    label=f"Promedio: ${promedio_ventas:,.0f}",
)

# Personalizar el título y etiquetas del gráfico principal
ax1.set_title(
    "Análisis de Rendimiento de Ventas Anuales",
    fontsize=20,
    fontweight="bold",
    pad=30,
    color="#2C3E50",
)
ax1.set_xlabel("Año", fontsize=14, fontweight="bold", color="#34495E")
ax1.set_ylabel("Ingresos ($)", fontsize=14, fontweight="bold", color="#34495E")

# Formatear el eje Y con separadores de miles y símbolo de dólar
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))

# Configurar la grilla del eje Y
ax1.grid(axis="y", alpha=0.3, linestyle="-", linewidth=0.5)
ax1.set_axisbelow(True)

# Mostrar la leyenda en la parte superior izquierda
ax1.legend(loc="upper left", fontsize=12, frameon=True, shadow=True)

# Quitar los bordes superior y derecho del gráfico
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.spines["left"].set_color("#BDC3C7")
ax1.spines["bottom"].set_color("#BDC3C7")

# Graficar la tasa de crecimiento anual en la subgráfica inferior
ax2.plot(
    crecimiento_anual.index[1:],
    crecimiento_anual.values[1:],
    marker="o",
    linewidth=3,
    markersize=8,
    color="#3498DB",
    markerfacecolor="#E74C3C",
    markeredgecolor="white",
    markeredgewidth=2,
)

# Dibujar una línea horizontal de referencia en 0%
ax2.axhline(y=0, color="#95A5A6", linestyle="-", linewidth=1, alpha=0.7)

# Personalizar el título y etiquetas del gráfico de crecimiento
ax2.set_title(
    "Tasa de Crecimiento Anual (%)", fontsize=14, fontweight="bold", color="#2C3E50"
)
ax2.set_xlabel("Año", fontsize=12, fontweight="bold", color="#34495E")
ax2.set_ylabel("Crecimiento (%)", fontsize=12, fontweight="bold", color="#34495E")

# Agregar el valor de crecimiento sobre cada punto (excepto el primer año)
for year, growth in crecimiento_anual.dropna().items():
    if year != crecimiento_anual.index[0]:  # Saltar el primer año
        ax2.text(
            year,
            growth + (max(crecimiento_anual.dropna()) * 0.1),
            f"{growth:.1f}%",
            ha="center",
            va="bottom",
            fontweight="bold",
            fontsize=10,
        )

# Agregar grilla y quitar bordes superiores y derechos
ax2.grid(True, alpha=0.3, linestyle="-", linewidth=0.5)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# Ajustar el diseño para evitar traslapes
plt.tight_layout()

# Calcular estadísticas clave para el resumen ejecutivo
total_ventas = ventasAnuales.sum()
mejor_año = ventasAnuales.idxmax()
peor_año = ventasAnuales.idxmin()

# Agregar un cuadro de texto con el resumen ejecutivo en la figura
fig.text(
    0.02,
    0.02,
    f"Resumen Ejecutivo:\n"
    f"• Ventas Totales: ${total_ventas:,.0f}\n"
    f"• Mejor Año: {mejor_año} (${ventasAnuales[mejor_año]:,.0f})\n"
    f"• Peor Año: {peor_año} (${ventasAnuales[peor_año]:,.0f})\n"
    f"• Promedio Anual: ${promedio_ventas:,.0f}",
    fontsize=11,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#ECF0F1", alpha=0.8),
    verticalalignment="bottom",
)

# Mostrar la figura final
plt.show()
#! Hay que preparar los datos para el clustering, usaremos la edad de los clientes y el beneficio que generan como características
x = df[["Customer_Age", "Profit"]]
"""
Escalar las características para que tengan la misma importancia en el clustering
El escalado consiste en cambiar los rangos de los datos, por ejemplo, 
si un campo tiene valores entre 0 y 100 y otro entre 0 y 1000, el segundo campo tendrá más peso en el clustering. 
Para evitar esto, escalamos los datos para que todos estén en un rango similar. 
Al escalar se pueden reducir o aumentar los valores de los datos.
"""
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
#? Encontramos el número optimo de grupos utilizando k el metodo del codo
axes = []
for i in range(1, 8):
    kmeans = KMeans(n_clusters=i,init='k-means++', random_state=42)
    kmeans.fit(x_scaled)
    axes.append(kmeans.inertia_)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\AZUser\Downloads\EVSales.csv")
df.shape
df.head()
df.info()
df.isnull().sum() 
df.columns
Tesla_cargaRapida = df[(df['Brand'] == 'Tesla') & (df['Fast_Charging_Option'] == 'Yes')]
TestlasumaUnidades = Tesla_cargaRapida['Units_Sold'].sum()
Region_promedio = df.groupby('Region')['Revenue'].mean().astype(int).reset_index()
#grafico de barras
plt.figure(figsize=(10, 6))
sns.barplot(data=Region_promedio, x='Region', y='Revenue')
plt.title('Promedio de Ingresos por Región')
plt.xlabel('Región')
plt.ylabel('Revenue Promedio en millones')
plt.show()

sns.histplot(data=df, x=df["Battery_Capacity_kWh"])
plt.title("Histograma de la capacidad de bateria en (kWh)")
plt.xlabel("Capacidad de Batería (kWh)")
plt.ylabel("Vecihulos")
plt.show()  # * muestra el histograma y quita etiquetas de los ejes 
sns.boxplot(
    data=df,
    x=df["Region"],  # * categoria para agrupar
    y=df["Discount_Percentage"],  # * campo a evaluar
)
plt.title("Boxplot de porcentaje de descuento por región")
plt.xlabel("Región")
plt.ylabel("Porcentaje de Descuento")
plt.show()  # * muestra el boxplot y quita etiquetas de los ejes

unidadesvendidas = df.groupby('Brand')['Units_Sold'].sum().reset_index()
# top 5 marcas con más unidades vendidas
top5_marcas = unidadesvendidas.nlargest(5, 'Units_Sold')
#barras horizontales
plt.figure(figsize=(10, 6))
sns.barplot(data=top5_marcas, x='Units_Sold', y='Brand')
plt.title('Top 5 Marcas con Más Unidades Vendidas')
plt.xlabel('Unidades Vendidas')
plt.ylabel('Marca')
plt.show()
#tipo de vehiculo con más unidades vendidas en norteamérica
tipo_vehiculo_norteamerica = df[df['Region'] == 'North America'].groupby('Vehicle_Type')['Units_Sold'].sum().reset_index()
# grafico de pastel
plt.figure(figsize=(8, 8))
plt.pie(tipo_vehiculo_norteamerica['Units_Sold'], labels=tipo_vehiculo_norteamerica['Vehicle_Type'], autopct='%1.1f%%', startangle=140)


#promedio de descuento por segmento 
promedioDescuento_segmento = df.groupby('Customer_Segment')['Discount_Percentage'].mean().round(3).reset_index()

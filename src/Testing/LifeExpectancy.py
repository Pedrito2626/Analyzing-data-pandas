import mlcroissant as mlc
import pandas as pd
import numpy as np
from scipy import stats  # * Libreria de estadística
import seaborn as sns
import matplotlib.pyplot as plt
import re

# ? Importar el dataset de esperanza de vida
croissant_dataset = mlc.Dataset(
    "https://www.kaggle.com/datasets/ignacioazua/life-expectancy/croissant/download"
)
record_sets = croissant_dataset.metadata.record_sets
print(record_sets)
recordSetsDF = pd.DataFrame(croissant_dataset.records(record_set=record_sets[0].uuid))
recordSetsDF.head()

recordSetsDF.rename(
    columns={
        "life_expectancy.csv/Country": "Country",
        "life_expectancy.csv/Sum+of+Females++Life+Expectancy": "Female Life Expectancy",
        "life_expectancy.csv/Sum+of+Males++Life+Expectancy": "Male Life Expectancy",
        "life_expectancy.csv/Sum+of+Life+Expectancy++(both+sexes)": "Both sex life expectancy",
    },
    inplace=True,
)
recordSetsDF.head()

# ? Define la expresión regular para encontrar los nombres de las columnas "b" y las comillas
pattern = r"b'(.*)"  # Encuentra el texto después de "b'" y antes de la comilla final

# ? Decodificar cadenas de bytes en cadenas normales antes de aplicar str.replace
recordSetsDF["Country"] = recordSetsDF[
    "Country"
].str.decode(  # ? utiliza utf-8 para decodificar
    "utf-8"
)

# ? Aplica la expresión regular para limpiar los nombres de las columnas
recordSetsDF.columns
recordSetsDF["Country"] = recordSetsDF[
    "Country"
].str.replace(  # ? Reemplaza "b'" y las comillas finales
    pattern, r"\1", regex=True
)

recordSetsDF[  # ? Filtra los registros donde la esperanza de vida femenina es 149.22}
    recordSetsDF["Female Life Expectancy"] == 149.22
]

# ? Reemplaza los valores erróneos en las columnas de esperanza de vida
recordSetsDF.replace({"Female Life Expectancy": {149.22: 74.82}}, inplace=True)
recordSetsDF.replace({"Male Life Expectancy": {137.64: 63.49}}, inplace=True)
recordSetsDF.replace({"Both sex life expectancy": {143.28: 71.3}}, inplace=True)
recordSetsDF.describe()

# ? Se saca la moda de la esperanza de vida femenina
mode_f = stats.mode(recordSetsDF["Female Life Expectancy"])
print(f"La moda en mujeres es de {mode_f.mode} años, con {mode_f.count} paises")
mode_b = stats.mode(recordSetsDF["Both sex life expectancy"])
print(f"La moda en ambos sexos es de {mode_b.mode} años, con {mode_b.count} paises")
mode_m = stats.mode(recordSetsDF["Male Life Expectancy"])
print(f"La moda en hombres es de {mode_m.mode} años, con {mode_m.count} paises")

sns.histplot(recordSetsDF["Female Life Expectancy"], kde=True, legend=False)
sns.histplot(recordSetsDF["Both sex life expectancy"], kde=True, legend=False)
sns.histplot(recordSetsDF["Male Life Expectancy"], kde=True, legend=False)
"""
curtosis:
La curtosis es una medida estadística que describe la forma de la distribución de datos,
especialmente en términos de la "altura" y "ancho" de sus colas. 
- Curtosis menor a 3: Colas más delgadas que una distribución normal, menos valores extremos.
- Curtosis mayor a 3: Colas más gruesas que una distribución normal, más valores extremos.
- Curtosis igual a 3: Colas similares a una distribución normal.
"""
CurtosisM = recordSetsDF["Male Life Expectancy"].kurt()
CurtosisF = recordSetsDF["Female Life Expectancy"].kurt()
CurtosisB = recordSetsDF["Both sex life expectancy"].kurt()
# ? Las 3 curtosis indican que es menos fácil encontrar valores extremos

PerCapitaDF = pd.read_csv(
    "C:\\Users\\AZUser\\Downloads\\archive (1)\\pib_per_capita_countries_dataset.csv"
)
PerCapitaDF = PerCapitaDF[PerCapitaDF["year"] == 2023]
PerCapitaDF.drop(
    columns=[
        "intermediate_region",
        "region",
        "sub_region",
        "indicator_code",
        "gdp_variation",
        "indicator_name",
    ],
    inplace=True,
)

#* Normalizar los nombres de los países: solo la primera letra en mayúscula
recordSetsDF["Country"] = recordSetsDF["Country"].str.title()
PerCapitaDF["country_name"] = PerCapitaDF["country_name"].str.title()
recordSetsDF["Country"] = recordSetsDF["Country"].str.strip()
PerCapitaDF["country"] = PerCapitaDF["country_name"].str.strip()

merged_df = pd.merge(
    recordSetsDF, PerCapitaDF, left_on="Country", right_on="country", how="inner"
)

merged_df.drop(columns=["country"], inplace=True)
#? Diagrama de dispersión con esperanza de vida femenina y PIB per cápita
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=merged_df,
    x="gdp_per_capita",
    y="Both sex life expectancy",
)
#* Correlacion entre PIB per cápita y esperanza de vida
correlation = merged_df["gdp_per_capita"].corr(merged_df["Both sex life expectancy"])
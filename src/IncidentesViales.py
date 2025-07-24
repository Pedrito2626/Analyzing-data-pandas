import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

x = pd.read_csv("C:\\Users\AZUser\Downloads\incidentes_viales.csv")
DatosIncidentesCopia = pd.DataFrame(x)
DatosIncidentesCopia.shape
DatosIncidentesCopia.head()
DatosIncidentesCopia.info()
DatosIncidentesCopia.describe()
DatosIncidentesCopia.isnull().sum()
DatosIncidentesCopia.columns
# ? Cambio de comuans y barrios porque son categoricas, tienen datos en común
DatosIncidentesCopia["NUMCOMUNA"] = DatosIncidentesCopia["NUMCOMUNA"].astype("category")
DatosIncidentesCopia["BARRIO"] = DatosIncidentesCopia["BARRIO"].astype("category")

# ? Cambiar la columna X, Y, que son coordenadas, a tipo int32
DatosIncidentesCopia["X"] = DatosIncidentesCopia["X"].astype("int32")
DatosIncidentesCopia["Y"] = DatosIncidentesCopia["Y"].astype("int32")

DatosIncidentesCopia["FECHA_ACCIDENTES"] = pd.to_datetime(
    DatosIncidentesCopia["FECHA_ACCIDENTES"]
)

# ?Visualizar valores únicos de todos los campos
col = DatosIncidentesCopia.columns
for c in col:
    print(f"Valores únicos de la columna {c}: {pd.unique(DatosIncidentesCopia[c])}")
for c in col:
    print(
        f"Porcentaje de valores nulos en la columna {c}: {DatosIncidentesCopia[c].isnull().sum() / len(DatosIncidentesCopia) * 100}"
    )

lista_barrios = list(pd.unique(DatosIncidentesCopia["BARRIO"]))
lista_comuna = list(pd.unique(DatosIncidentesCopia["COMUNA"]))
"""
Cambiar letras donde no se identifican tildes
cambiar 0 por nulo
cambiar sin inf por nulo
cambiar au por nulo
cambiar numero del codigo por barrio
cambiar nan por none
"""

DatosIncidentesCopia["BARRIO"] = DatosIncidentesCopia["BARRIO"].str.lower()
DatosIncidentesCopia["COMUNA"] = DatosIncidentesCopia["COMUNA"].str.lower()
valores_reemplazar = [
    "Caida Ocupante",
    "Caída Ocupante",
    "Caída de Ocupante",
    "Caida de Ocupante",
]
DatosIncidentesCopia.replace(valores_reemplazar, "Caida Ocupante", inplace=True)

# ? Expresiones regulares para reemplazar caracteres especiales
DatosIncidentesCopia.replace(
    {
        r"\\xe1": "á",
        r"\\xe9": "é",
        r"\\xed": "í",
        r"\\xf3": "ó",
        r"\\xF3": "ó",
        r"\\xfa": "ú",
        r"\\xf1": "ñ",
        r"\\xc1": "A",
        r"\\xF1": "ñ",
    },
    regex=True,
    inplace=True,
)
lista_barrios
url_barrios = "https://www.medellin.edu.co/?sdm_process_download=1&download_id=10121"
dfBarrios = pd.read_excel(
    url_barrios, sheet_name="Código barrios", usecols=[0, 1], header=3, dtype=str
)
dfBarrios["Sin especificar"] = dfBarrios["Sin especificar"].str.lower()
diccionario_barrios = dfBarrios.set_index(dfBarrios.columns[0])[
    dfBarrios.columns[1]
].to_dict()
DatosIncidentesCopia.replace(diccionario_barrios, inplace=True)

lista_barrios_m = list(pd.unique(DatosIncidentesCopia["BARRIO"]))
pd.unique(DatosIncidentesCopia["COMUNA"])
valores_reemplazar = [
    "inst",
    "Sin Inf",
    "nan",
    "sin inf",
    "0",
    "AU",
    "au",
    "In",
    "SN",
    "in",
    "sn",
    "No Georef",
    "auc1",
    "auc2",
    "no georef",
    "AUC2",
    "AUC1",
    "INST",
    "9086",
]
DatosIncidentesCopia.replace(valores_reemplazar, None, inplace=True)
DatosIncidentesCopia.groupby(["BARRIO"]).size().sort_values(ascending=False)
DatosIncidentesCopia.groupby(["COMUNA"]).size().sort_values(ascending=False)
DatosIncidentesCopia.groupby(["CLASE_ACCIDENTE"]).size().sort_values(ascending=False)
DatosIncidentesCopia.groupby(["GRAVEDAD_ACCIDENTE"]).size().sort_values(ascending=False)

Top10 = DatosIncidentesCopia.groupby(["COMUNA", "GRAVEDAD_ACCIDENTE"]).size().sort_values(
    ascending=False
).head(10)

sns.histplot(data= DatosIncidentesCopia,
             x = "COMUNA",
             hue= "GRAVEDAD_ACCIDENTE",
             multiple="stack"
)
plt.title("Gravedad de incidentes por comuna")
plt.xticks(rotation=90)
plt.show()

sns.histplot(data= DatosIncidentesCopia,
             x = "DISEÑO",
             hue= "GRAVEDAD_ACCIDENTE",
             multiple="stack"
)
plt.title("Gravedad de incidentes por comuna")
plt.xticks(rotation=90)
plt.show()
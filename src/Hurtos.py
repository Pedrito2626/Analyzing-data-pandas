import pandas as pd

"""
Para los 3 datasets:
Limpieza de datos
Identificar si el barrio y la comuna donde más casos de hurto hay 
    es el mismo para los 3 datasets
"""
x = pd.read_csv("C:\\Users\\AZUser\\Downloads\\hurto_a_persona.csv")
y = pd.read_csv("C:\\Users\\AZUser\\Downloads\\hurto_a_establecimiento_comercial.csv")
z = pd.read_csv("C:\\Users\\AZUser\\Downloads\\hurto_de_moto.csv")

HurtoPersona = pd.DataFrame(x)
HurtoEstablecimiento = pd.DataFrame(y)
HurtoMoto = pd.DataFrame(z)
HurtoPersona.drop(
    columns=[
        "grupo_actor",
        "actividad_delictiva",
        "parentesco",
        "ocupacion",
        "discapacidad",
        "grupo_especial",
        "nivel_academico",
        "testigo",
        "caracterizacion",
        "articulo_penal",
        "categoria_penal",
        "permiso",
        "unidad_medida",
    ],
    inplace=True,
)
HurtoPersona.shape
HurtoPersona.head()
HurtoPersona.info()
HurtoPersona.describe()
HurtoPersona.isnull().sum()
HurtoPersona["latitud"].fillna(0, inplace=True)
HurtoPersona["longitud"].fillna(0, inplace=True)

HurtoEstablecimiento.drop(
    columns=[
        "grupo_actor",
        "sexo",
        "estado_civil",
        "actividad_delictiva",
        "parentesco",
        "ocupacion",
        "discapacidad",
        "grupo_especial",
        "nivel_academico",
        "testigo",
        "caracterizacion",
        "articulo_penal",
        "categoria_penal",
        "permiso",
        "unidad_medida",
        "color",
    ],
    inplace=True,
)
HurtoEstablecimiento.shape
HurtoEstablecimiento.head()
HurtoEstablecimiento.info()
HurtoEstablecimiento.describe()
HurtoEstablecimiento.isnull().sum()
HurtoEstablecimiento["latitud"].fillna(0, inplace=True)
HurtoEstablecimiento["longitud"].fillna(0, inplace=True)

HurtoMoto.drop(
    columns=[
        "grupo_actor",
        "actividad_delictiva",
        "parentesco",
        "ocupacion",
        "discapacidad",
        "grupo_especial",
        "nivel_academico",
        "testigo",
        "caracterizacion",
        "articulo_penal",
        "categoria_penal",
        "permiso",
        "unidad_medida",
    ],
    inplace=True,
)
HurtoMoto.shape
HurtoMoto.head()
HurtoMoto.info()
HurtoMoto.describe()
HurtoMoto.isnull().sum()
HurtoMoto["latitud"].fillna(0, inplace=True)
HurtoMoto["longitud"].fillna(0, inplace=True)

import pandas as pd

hospital_dfPrueba = pd.DataFrame(
    data=[
        [16, 1.6, " ", "Sossa", "Trauma"],
        [20, 1.7, "Nicolas", "Gaviria", "Cuadro viral"],
        [15, "", "Daniela", "Ramirez", "Gastritis"],
        [18, 1.72, "Sandra", "NaN", " "],
    ],
    columns=["Edad", "Altura", "Nombre", "Apellido", "Diagnóstico"],
    index=["Paciente1", "Paciente2", "Paciente3", "Paciente4"],
)
hospital_dfPrueba.isnull()
hospital_dfPrueba.isnull().sum()
#! Visualizar registros dentro de un campo
valores_altura = list(hospital_dfPrueba["Altura"].unique())
hospital_dfPrueba["Nombre"].unique()
hospital_dfPrueba["Apellido"].unique()

# * Nulos en python: None y np.nan
#! Limpieza de datos
hospital_dfPrueba = hospital_dfPrueba.replace(
    "", None
)  # ? Estructura replace (valor_a_reemplazar, nuevo_valor)
hospital_dfPrueba = hospital_dfPrueba.replace(" ", None)  # ? Reemplazar " " por None
hospital_dfPrueba = hospital_dfPrueba.replace(
    "NaN", None
)  # ? Reemplazar "NaN" por None
hospital_dfPrueba.fillna("Relleno")  # ? Rellenar los nulos con un valor específico

promedioAlt = hospital_dfPrueba["Altura"].mean().round(2)
hospital_dfPrueba["Altura"].fillna(
    promedioAlt
)  # ? En caso de querer cambiarlo definitivamente, se coloca inplace=True
nombre = ["Mateo", "Ramirez"]
for indice, valor in enumerate(
    nombre
):  # * Permite visualizar el índice y el valor de los elementos de la lista
    print(indice, valor)
string = "Hola, soy un string"
listaP = string.split()  # * Permite separar un string en una lista

# TODO: Separar los apellidos de los pacientes en dos columnas diferentes
hospital_df_sep_val = pd.DataFrame(
    data=[
        [16, 1.6, "Luis", "Sossa Ramirez", "", "Trauma"],
        [20, 1.7, "Nicolas", "", "Aguirre", "Cuadro viral"],
        [15, "", "Daniela", "Ramirez Valencia", "", "Gastritis"],
        [18, 1.72, "Sandra", "Nan", "Rojas", " "],
        [19, 1.82, "Simon", "Alvarez Pineda", "", "Cuadro viral"],
        [22, 1.74, "Sergio", "Alvarez Pineda", "", "Cuadro viral"],
    ],
    columns=[
        "Edad",
        "Altura",
        "Nombre",
        "Primer apellido",
        "Segundo apellido",
        "Diagnotisco",
    ],
    index=[
        "Paciente1",
        "Paciente2",
        "Paciente3",
        "Paciente4",
        "Paciente5",
        "Paciente6",
    ],
)
# ? Reemplazo individual de valores

# * hospital_df_sep_val = hospital_df_sep_val.replace("", None) Reemplazar "" por None
# * hospital_df_sep_val = hospital_df_sep_val.replace(" ", None) Reemplazar " " por None
# * hospital_df_sep_val = hospital_df_sep_val.replace("Nan", None) Reemplazar "Nan" por None

# ? O, se pueden reemplazar varios valores a la vez:
hospital_df_sep_val = hospital_df_sep_val.replace(["", " ", "Nan"], None)
for i in hospital_df_sep_val["Primer apellido"].index:
    if hospital_df_sep_val["Primer apellido"][i] is not None:
        apellido = hospital_df_sep_val["Primer apellido"][i].split()
        if len(apellido) > 1:
            hospital_df_sep_val.at[i, "Primer apellido"] = apellido[0]
            hospital_df_sep_val.at[i, "Segundo apellido"] = apellido[1]
        else:
            hospital_df_sep_val.at[i, "Primer apellido"] = apellido[0]
            hospital_df_sep_val.at[i, "Segundo apellido"] = None

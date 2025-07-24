import numpy as np
from scipy import stats

"""
Metodlogia:
Hipotesis Nula (H0): No hay diferencia en al reduccion de la presion arterial entre los dos grupos.
Hipotesis Alternativa (H1): Hay una diferencia en la reduccion de la presion arterial entre los dos grupos.

"""
# * Recopilación de datos
grupo_medicamento = np.array([130, 125, 140, 118, 124, 134, 128, 136, 130, 129])
grupo_placebo = np.array([140, 142, 138, 150, 139, 142, 137, 148, 142, 141])

# * Elección de un nivel de significancia
# ? p_valor = 0.05

# * Calculo de la estadistica p_valor
t_stat, p_valor = stats.ttest_ind(grupo_medicamento, grupo_placebo)

# * Toma de Decisión
if p_valor < 0.05:
    print("Se rechaza la Hipotesis Nula (H0)")
else:
    print("No se rechaza la Hipotesis Nula (H0)")

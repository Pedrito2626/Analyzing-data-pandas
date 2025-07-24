import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from scipy.stats import norm, kurtosis

sns.set_style("whitegrid")
sns.set_palette("husl")
mat_data = pd.read_csv("C:\\Users\\AZUser\\Downloads\\student-mat.csv", sep=";")
por_data = pd.read_csv("C:\\Users\\AZUser\\Downloads\\student-por.csv", sep=";")

mat_data.shape, por_data.shape
mat_data.head()
por_data.head()
mat_data.info()
por_data.info()
mat_data.describe()
por_data.describe()
mat_data.isnull().sum()
por_data.isnull().sum()


# ? Definimos una función para realizar las graficas de histogramas y boxplots
def plot_histograms_boxplots(data, columns, dataset_name):
    fig, axes = plt.subplots(len(columns), 2, figsize=(12, 4 * len(columns)))
    for i, column in enumerate(columns):
        sns.histplot(data[column], kde=True, ax=axes[i, 0])
        axes[i, 0].set_title(f"{dataset_name} - Histogram of {column}")

        sns.boxplot(x=data[column], ax=axes[i, 1])
        axes[i, 1].set_title(f"{dataset_name} - Boxplot of {column}")
    plt.tight_layout()


# ? Columnas de interés
columns = ["age", "studytime", "failures", "G1", "G2", "G3"]

# ? Graficando dataset estudiantes de matemáticas
plot_histograms_boxplots(mat_data, columns, "Mathematics")

# ? Curtosis
variables = ["age", "studytime", "failures", "G1", "G2", "G3"]
for i in variables:
    print(f"Curtosis de {i}: {kurtosis(mat_data[i])}")

# ? Graficando dataset estudiantes de portugues
plot_histograms_boxplots(por_data, columns, "Portuguese")

# ? Curtosis
for i in variables:
    print(f"Curtosis de {i}: {kurtosis(por_data[i])}")

# ? Tabla de frecuencias
contingency_table = pd.crosstab(mat_data["schoolsup"], mat_data["G3"])

chi2, p, dof, expected = chi2_contingency(contingency_table)
print(
    f"Chi-squared: {round(chi2, 3)}, p-value: {round(p, 3)}, Degrees of freedom: {dof}"
)

aspect_to_test = {
    "School Support and Academic Performance": ("schoolsup", "G3"),
    "Family Support and Grades": ("famsup", "G3"),
    "Extra-Curricular Activities and Performance": ("activities", "G3"),
    "Romantic Relationships and Academic Performance": ("romantic", "G3"),
    "Health Status and Grades": ("health", "G3"),
}
for aspect, columns in aspect_to_test.items():
    print(aspect, columns)
    columna_0 = columns[0]
    columna_1 = columns[1]
    contingency_table = pd.crosstab(mat_data[columna_0], mat_data[columna_1])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    significance = "Significant" if p < 0.05 else "Not Significant"
    print(
        f"Chi-squared: {round(chi2, 3)}, p-value: {round(p, 3)}, Degrees of freedom: {dof}, Significance: {significance}\n"
    )

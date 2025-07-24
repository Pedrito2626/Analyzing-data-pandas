# Data Analysis Portfolio with Python
This repository presents a collection of data analysis projects, where various concepts and techniques are applied using Python and its specialized libraries. The main objective is to demonstrate skills in data manipulation, visualization, statistical analysis, and modeling across different datasets.

## Features and Concepts Applied:
The project covers a wide range of data analysis and machine learning techniques, including:

- Exploratory Data Analysis (EDA): Data cleaning, preprocessing, and transformation, handling null and duplicate values.

- Data Visualization: Creation of various charts (histograms, box plots, scatter plots, heatmaps, etc.) to identify patterns, trends, and relationships.

- Descriptive and Inferential Statistics: Calculation of measures of central tendency, dispersion, correlation (Pearson, Chi-squared), kurtosis, and hypothesis testing.

- Feature Engineering: Data preparation for modeling, including categorical variable encoding (Label Encoding) and feature scaling (StandardScaler).

- Machine Learning Modeling:

    - Regression: Simple Linear Regression, Ridge, Lasso, ElasticNet.

    - Trees and Ensembles: RandomForestRegressor.

    - Clustering: K-Means for customer segmentation.

- Dimensionality Reduction: Principal Component Analysis (PCA).

- Model Evaluation: Metrics such as R2_score, Mean Absolute Error (MAE), Mean Squared Error (MSE), and cross-validation.

## Datasets Analyzed:
Multiple databases from various domains are used and analyzed, including:

- Vehicle CO2 Emissions (Emissions_Canada_CO2.csv): Analysis of the relationship between engine size, fuel type, and CO2 emissions.

- Commercial Performance (sales_data.csv): Analysis of annual and monthly sales, customer profiling, product performance, and sales location.

- Student Performance (student-mat.csv, student-por.csv, BD_LISTA.xlsx): Exploration of factors influencing academic performance, with correlation and distribution analysis.

- Air Quality (Air_Quality.csv): Identification of pollutants by city and temporal trends.

- EV Sales (EVSales.csv): Analysis of electric vehicle sales by region, brand, and battery capacity.

- Road Incidents (incidentes_viales.csv): Exploration of road incidents, including areas with higher occurrence and related variables.

- Theft Data (hurto_a_persona.csv, hurto_a_establecimiento_comercial.csv, hurto_de_moto.csv): Analysis of theft patterns by type, neighborhood, and commune.

- GDP per Capita (pib_per_capita_countries_dataset.csv): Relationship between life expectancy and GDP per capita.

- Housing Prices (train.csv, test.csv): Analysis of factors influencing housing prices and construction of predictive models.

- Iris Dataset: Exploration of relationships between flower characteristics.

- CO2 Dataset (statsmodels.api.co2): Analysis of atmospheric CO2 concentration.

- tips Dataset: Analysis of restaurant tip data.

- Null Data Handling: Practical examples of identifying and handling various types of null values (NaN, blanks) in DataFrames, a crucial step in data cleaning.

## Project Structure:
This project follows an organized structure to facilitate navigation and understanding:
```
├── LICENSE <- Open-source license (MIT License)
├── README.md <- This file, the high-level project description.
├── data
│   ├── external <- Third-party data
│   ├── interim <- Intermediate data that has been transformed
│   ├── processed <- Final, canonical datasets for modeling
│   └── raw <- Original and immutable data
├── models <- Trained and serialized models
├── notebooks <- Jupyter notebooks containing analysis and development.
│   ├── 02_ML.ipynb <- Main Machine Learning notebook.
│   ├── contrasena.ipynb <- Password validation example (utility use).
│   ├── idk.ipynb <- Example notebook with basic operations.
│   └── emisiones-y-nba.ipynb <- CO2 emissions and NBA data analysis.
├── requirements.txt <- Project dependencies
└── src <- Python scripts with modular and reusable source code.
    ├── Chi-squared.py <- Chi-squared test implementation.
    ├── Estadistica.py <- Basic statistics concepts.
    ├── HousingPrices.py <- Housing price analysis.
    ├── Hurtos.py <- Theft data analysis.
    ├── IncidentesViales.py <- Road incident analysis.
    ├── RendimientoComercial.py <- Commercial performance analysis.
    ├── Surveillance.py <- Surveillance data analysis.
    ├── Testing <- Subdirectory for concept testing scripts.
    │   ├── CALIDAD_AIRE_dataset.py <- Air quality dataset analysis.
    │   ├── Correlacion.py <- Correlation analysis.
    │   ├── Curtosis.py <- Kurtosis calculation and analysis.
    │   ├── EVsales.py <- Electric vehicle sales analysis.
    │   ├── Estudiantes.py <- Student dataset analysis.
    │   ├── Iris.py <- Iris dataset analysis.
    │   ├── nullData.py <- Null data handling.
    │   └── tips.py <- Tips dataset analysis.
    ├── emisiones-y-nba.ipynb (copy)
    ├── graficas.py <- Examples and functions for various plots.
    └── pca.py <- PCA implementation
````
### Technologies Used:
Python 3.11.5

## Main Libraries:

- pandas: For data manipulation and analysis.

- numpy: For numerical operations.

- matplotlib: For static data visualization.

- seaborn: For statistical data visualization.

- plotly: For interactive visualizations.

- scipy: For statistical and scientific functions.

- scikit-learn: For machine learning (preprocessing, modeling, evaluation).

- statsmodels: For statistical models and tests.

- yellowbrick: For ML model evaluation visualizations.

- mlcroissant: For Croissant datasets.

## How to Run the Project:
Clone the repository:

**Bash**

git clone https://github.com/pedrito2626/analyzing-data-pandas
cd analyzing-data-pandas
Set up the virtual environment and install dependencies:
**It is recommended to use a virtual environment to avoid dependency conflicts.**

**Bash**

python -m venv env
**On Windows:**
.\env\Scripts\activate
**On macOS/Linux:**
source env/bin/activate

pip install -r requirements.txt
Duplicate the .env.example file:
**You will need to create a .env file for your environment variables, such as API credentials if necessary (although this project does not seem to have a direct dependency on external APIs requiring keys).**

**Bash**

cp .env.example .env # For Linux, macOS, Git Bash, WSL
copy .env.example .env # For Windows Command Prompt
Run the notebooks:
You can open and run the Jupyter notebooks (.ipynb) from the terminal:

**Bash**

jupyter notebook
This will open Jupyter in your browser, where you can navigate to the notebooks folder and run the analyses.

## Key Findings and Featured Projects (Examples):
While each notebook contains specific analyses, some highlights include:

- CO2 Emissions Analysis: A clear linear relationship is observed between engine size and CO2 emissions. Vehicles with fuel type 'Z' (premium gasoline) and 'X' (regular gasoline) show different ranges of emissions and engine sizes, with 'Z' generally having larger engines and higher emissions.

- Commercial Performance: Sales analysis over the years reveals seasonality and growth trends. Customer segmentation by age and profit provides valuable insights for marketing strategies. Visualizing sales by category and subcategory helps identify profitable products.

- Null Data Analysis: Demonstrates how to identify and handle different types of null values (NaN, blank spaces) in DataFrames, a crucial step in data cleaning.

- Correlation Analysis: Visual examples of correlation matrices to understand the relationship between variables in different datasets, such as the relationship between CO2 concentration over time.

## License
This project is licensed under the MIT License.

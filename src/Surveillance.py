import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
df = pd.read_csv("C:\\Users\\AZUser\\Downloads\\brfss2022.csv")
df
df.shape
df.info()
df.describe()
df.isnull().sum()
#
#? Correlación
correlation_matrix = df.corr()
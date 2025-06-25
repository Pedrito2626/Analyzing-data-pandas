import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dfTips = sns.load_dataset("tips")
dfTips.head()
dfTips.describe()
dfTips.info()
dfTips.isnull().sum()
numtips = dfTips.select_dtypes(include=[np.number])
sns.heatmap(numtips.corr(), annot=True, cmap='coolwarm')
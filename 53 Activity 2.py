import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

HouseDF=pd.read_csv('USA_Housing.csv')
HouseDF.head()
HouseDF.info()
HouseDF.describe()
HouseDF.columns
sns.pairplot(HouseDF)
numeric_df = HouseDF.select_dtypes(include=['int64', 'float64'])

sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
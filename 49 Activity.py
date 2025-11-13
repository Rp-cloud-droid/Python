import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("country_vaccinations.csv")
print(df.head(10))

print(df.isnull().sum())

missing_value=["N/a", "na", np.nan]
df=pd.read_csv("country_vaccinations.csv", na_values=False)

print(df.isnull().sum())

print(df.isnull().any())

subset = df.iloc[:5200, :]
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

print(df.head(10))

print(df.dropna())

print(df.dropna(how="all"))

print(df.fillna(0))

print(df.fillna(method="bfill"))

print(df.interpolate())

df_dropped=df.dropna()
print(df_dropped)
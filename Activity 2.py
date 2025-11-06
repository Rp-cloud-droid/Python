import pandas as pd
import seaborn as sb
import numpy as np
from matplotlib import pyplot as plt

print("Loading built-in 'iris' dataset...")
df = sb.load_dataset("iris")

print("\nSample of built-in dataset:")
print(df.head())

sb.displot(df['petal_length'], kde=True)
plt.title("Distribution of Petal Length (Built-in Iris Dataset)")
plt.show()

print("\nLoading local Iris.csv file (if avaiable)...")
df_local = pd.read_csv("Iris.csv")
print("\nSample of local dataset:")

df = sb.load_dataset('iris')
sb.distplot(df['petal_length'], hist=False)
plt.show

sb.jointplot(x='petal_length', y='petal_length', data=df)
plt.show()

sb.set_style("ticks")
sb.pairplot(df, hue='species', diag_kind="kde", kind="scatter", palette="husl")
plt.show()

uniform_data = np.random.rand(10, 12)

ax = sb.heatmap(uniform_data)
plt.show()
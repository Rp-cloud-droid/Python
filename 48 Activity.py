import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\Users\rupal\OneDrive\Desktop\Web Developement\Coding\Python\Lesson 48\penguins_size.csv")

print(df.read(10))

print(df.shape)
print(df.tail())
print(df.isnull().sum())

print(df.describe().T)
print(df.describe(include="all"))

print(df.dtypes)
print(df.info())

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True), cmap="Wistia", annot=True)

df.hist(figsize=(12, 9))
plt.show()

print(df['sex'].value_counts())
print(df['island'].value_counts())
print(df['species'].value_counts())

sns.countplot(data=df, x="sex", palette="summer")
plt.show()

sns.countplot(data=df, x="island", palette="RdPu")
plt.show()

sns.countplot(data=df, x="species", palette="YlORd")
plt.show()

sns.countplot(data=df, x="island", hue="sex", palette="spring")
plt.show()

sns.pairplot(data=df, hue="species", palette="mako")
plt.show()
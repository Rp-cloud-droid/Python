import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

weather = pd.read_csv(r"C:\Users\rupal\OneDrive\Desktop\Web Developement\Coding\Python\Lesson 47\Weather Dataset - Trial Activity DataSet.csv.csv")
print(weather.head())
print(weather.info())

sns.barplot(x='humidity', y='temperature', data=weather)
plt.show()

sns.histplot(weather['humidity'], kde=True)
plt.show()

sns.histplot(weather['humidity'])
sns.rugplot(weather['humidity'])
plt.show()

sns.jointplot(x='humidity', y='temperature', data=weather)
sns.jointplot(x='humidity', y='temperature', data=weather, kind="hex")
sns.jointplot(x='humidity', y='temperature', data=weather, kind="kde")

sns.pairplot(weather[['humidity', 'temperature']])
plt.show()

sns.stripplot(x='weather_type', y='temperature', data=weather)
plt.show()

sns.swarmplot(x='weather_type', y='temperature', data=weather)
plt.show()

sns.boxplot(x='weather_type', y='temperature', data=weather)
plt.show()

sns.barplot(x='weather_type', y='temperature', data=weather)
plt.show()

sns.countplot(data=weather["humidity"])
plt.show()
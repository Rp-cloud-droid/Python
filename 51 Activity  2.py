import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('Countries Data.csv')
countries = countries_df
print(countries.head())

c_52 = countries.loc[countries['year'] == 1952]
print(c_52.head())

c_07 = countries.loc[countries['year'] == 2007]
print(c_07.head())

c_merge = c_52.merge(c_07, left_on='country', right_on='country')
print(c_merge.head())

print(c_merge.drop(['year_x', 'year_y'], axis=1))
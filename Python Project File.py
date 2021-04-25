import pandas as pd

movies=pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")
print(movies.head())
print(movies.tail())
print(movies.info())

print(movies['Type'].value_counts())

movies.drop('Type',axis='columns',inplace=True)
print(movies.info())

print(movies.isnull().sum())
print(movies['IMDb'].mean())
print(movies['IMDb'].median())
print(movies['IMDb'].min())
print(movies['IMDb'].max())
print(movies['IMDb'].value_counts())


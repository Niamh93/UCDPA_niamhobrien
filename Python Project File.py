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


movies['IMDb']=movies['IMDb'].fillna(movies['IMDb'].median())
print(movies.info())
print(movies['IMDb'].mean())

Netflix=movies[movies['Netflix']==1]
print(Netflix.info())

Hulu=movies[movies['Hulu']==1]
print(Hulu.info())

Prime=movies[movies['Prime Video']==1]
print(Prime.info())

Disney=movies[movies['Disney+']==1]
print(Disney.info())




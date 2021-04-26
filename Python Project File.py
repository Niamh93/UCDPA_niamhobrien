import pandas as pd
import matplotlib.pyplot as plt

movies=pd.read_csv("MoviesOnStreamingPlatforms_updated.csv",index_col='ID')
print(movies.head())
print(movies.tail())
print(movies.info())

print(movies['Type'].value_counts())

movies.drop(['Unnamed: 0','Type','Rotten Tomatoes','Directors','Country','Language','Runtime'],axis='columns',inplace=True)
print(movies.info())

print(movies.isnull().sum())
print(movies['IMDb'].mean())
print(movies['IMDb'].median())
print(movies['IMDb'].min())
print(movies['IMDb'].max())
print(movies['IMDb'].value_counts())


movies['IMDb']=movies['IMDb'].fillna(movies['IMDb'].median())
print(movies.info())
mean_IMDb = movies['IMDb'].mean()
print(mean_IMDb)

Netflix=movies[movies['Netflix']==1]
print(Netflix.info())

Hulu=movies[movies['Hulu']==1]
print(Hulu.info())

Prime=movies[movies['Prime Video']==1]
print(Prime.info())

Disney=movies[movies['Disney+']==1]
print(Disney.info())

movies_sorted=movies.sort_values(by=['Year'])
print(movies_sorted.head())
print(movies['Year'].min())
print(movies['Year'].max())

#plot 1 showing the number of movies per year
movies['Year'].hist(bins=20)
plt.show()

List1=[Netflix['IMDb'].mean(),Hulu['IMDb'].mean(),Prime['IMDb'].mean(),Disney['IMDb'].mean()]
func1=lambda x : x-mean_IMDb
List2=list(map(func1,List1))
print(List1)
print(List2)

def pct25(column):
    return column.quantile(0.25)
def pct75(column):
    return column.quantile(0.75)

List3=[Netflix['IMDb'].agg([pct25,pct75]),Hulu['IMDb'].agg([pct25,pct75]),Prime['IMDb'].agg([pct25,pct75]),Disney['IMDb'].agg([pct25,pct75])]
print(List3)

fig,ax=plt.subplots()
ax.bar('Netflix',Netflix['IMDb'].mean(),yerr=Netflix['IMDb'].std())
ax.bar('Hulu',Hulu['IMDb'].mean(),yerr=Hulu['IMDb'].std())
ax.bar('Prime',Prime['IMDb'].mean(),yerr=Prime['IMDb'].std())
ax.bar('Disney',Disney['IMDb'].mean(),yerr=Disney['IMDb'].std())
ax.bar('All Services',movies['IMDb'].mean(),yerr=movies['IMDb'].std())
ax.set_ylabel("IMDb rating")
plt.show()

fig,ax=plt.subplots()
ax.boxplot([Netflix['IMDb'],Hulu['IMDb'],Prime['IMDb'],Disney['IMDb'],movies['IMDb']])
ax.set_xticklabels(['Netflix','Hulu','Prime','Disney','Movies'])
ax.set_ylabel('IMDb rating')
plt.show()


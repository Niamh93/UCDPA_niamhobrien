import pandas as pd
import matplotlib.pyplot as plt

movies=pd.read_csv("MoviesOnStreamingPlatforms_updated.csv",index_col='ID')
print(movies.head())
print(movies.tail())
print(movies.info())

print(movies['Type'].value_counts())

movies.drop(['Unnamed: 0','Type','Rotten Tomatoes','Directors','Country','Language','Runtime','Genres'],axis='columns',inplace=True)
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

#plot showing ratings from each streamling service
fig,ax=plt.subplots()
ax.boxplot([Netflix['IMDb'],Hulu['IMDb'],Prime['IMDb'],Disney['IMDb'],movies['IMDb']])
ax.set_xticklabels(['Netflix','Hulu','Prime','Disney','Movies'])
ax.set_ylabel('IMDb rating')
fig.suptitle('Movie Ratings by streaming service')
plt.show()

#plot showing the number of movies per year
fig,ax=plt.subplots()
ax.hist(movies['Year'],bins=20)
ax.set_xlabel('Number of Movies')
ax.set_ylabel('Year')
fig.suptitle('Movies per Year')
plt.show()

fig,ax=plt.subplots()
ax.boxplot([Netflix['Year'],Hulu['Year'],Prime['Year'],Disney['Year'],movies['Year']])
ax.set_xticklabels(['Netflix','Hulu','Prime','Disney','Movies'])
ax.set_ylabel('Year released')
fig.suptitle('Number of Movies per Year')
plt.show()

def min(column):
    return column.min()
def max(column):
    return column.max()

min_rates=[]
max_rates=[]
x=movies['Year'].min()
print(x)
while x < 2021:
    if x in movies['Year']:
        a = movies[movies['Year']==x]['IMDb'].min()
        b = movies[movies['Year'] == x]['IMDb'].max()
        min_rates.append(a)
        max_rates.append(b)
        x=(x+1)

    else:
        x=(x+1)

min_rates=[min_rates for min_rates in min_rates if str(min_rates) !='nan']
max_rates=[max_rates for max_rates in max_rates if str(max_rates) !='nan']
Year=movies_sorted['Year'].drop_duplicates()
print(Year)

fig,ax=plt.subplots()
ax.scatter(movies_sorted['Year'],movies_sorted['IMDb'],alpha=0.3)
ax.set_label('Year released')
ax.set_ylabel('IMDb rating')
fig.suptitle('Movie Ratings by Year')
plt.plot(Year,min_rates,color='purple',linestyle='--',linewidth=1)
plt.plot(Year,max_rates,color='green',linestyle='--',linewidth=2)

plt.show()

#merge 4 streaming services together and check for duplicates
merged_services=pd.concat([Netflix,Hulu,Prime,Disney],ignore_index=False,keys=['N','H','P','D'])
print(merged_services.info())
print(merged_services['Title'].count()-merged_services['Title'].nunique())

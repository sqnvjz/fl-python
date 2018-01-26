import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# path = '/Users/yujiezhang/source/practices/fluentpython/pandas/tmdb_5000_movies.csv'
# df = pd.read_csv(path)

# print(df.shape)
# print(df.columns)


# df_new = df[['popularity','id','vote_count']]
#
# print(df_new.iloc[10:20,0:2])

# print(df.head())

# s1 = Series([1,2,3,4], index=['A','N','D','H'])
# s2 = s1.reindex(index=['A','N','D','H','L','P'], fill_value={'L':2, 'P':3})

# s1 = Series(['A','N','D','H'], index=[1,4,7,11])
# s2 = s1.reindex(index=np.arange(15), method='ffill')
# print(s2)

df = DataFrame(np.random.rand(25).reshape([5,5]), index=[1,2,3,4,5], columns=['B1','B2','B3','B4','B5'])

# print(df)


# df = DataFrame([[1,2,3,4],[2,3,4,np.nan],[3,5,np.nan,7]])
# df1 = df.fillna({2:2,3:3})
# print(df)
# print(df1)

# s1 = Series(np.random.randn(6), index=[['1','1','1','2','2','2'],['a','b','c','a','b','c']])
# print(s1[:,'a'])
# print(s1)
# df1 = s1.unstack()
# print(df1)

# s2 = df1.T.unstack()
# print(s2)


# df1 = DataFrame({'city':['BJ','SH','GZ'], 'population':[1000,1200,1300]})
# df1['GDP'] = Series([200,400,800])
# print(df1)

s1 = Series(np.arange(10))
s2 = s1.replace({1:2,2:3,3:4})
print(s2)
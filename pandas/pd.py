import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# s = pd.Series(np.arange(15))
# print(s.values)

# s2 = pd.Series(np.arange(4), index=['A', 'B', 'C', 'D'])
# # print(s2[s2!=3])
#
# s3 = pd.Series(s2.to_dict())
# print(isinstance(s2, pd.core.series.Series))

# import webbrowser
# link = 'https://www.tiobe.com/tiobe-index'
# webbrowser.open(link)
import pickle
# df1 = pd.read_clipboard()
# f = open('df.b', 'wb')
# pickle.dump(df1, f)

# f = open('df.b', 'rb')
# df = pickle.load(f)
# df = np.load('df.npy')
# print(type(df))
# print(df.columns)
# print(type(df['Programming Language']))
# df_new = DataFrame(df, columns=['Programming Language', 'Jan 2018'])
# print(df_new)
# a = np.arange(20)
# print(a)

# print(df)

# df.to_csv('df.csv', index=False)
file_csv = 'df.csv'
df2 = pd.read_csv(file_csv)
# print(df2)
# j = df2.to_json()
# print(j)

# file_html = 'df.html'
# df2.to_html(file_html)

df2.to_excel('df.xlsx')
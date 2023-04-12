#data frame
#head
#tail
#column
#dtype
#calculate missing values


import numpy as np
import  pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/missing_data1.csv',sep=',')
print(df)
print(df.head)
print(df.tail)
print(df.dtypes)
print(df.columns)
print(df.isna().sum())
df1=(df.fillna('india'))
print(df1)

print(df1.isna().sum())

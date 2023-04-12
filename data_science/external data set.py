#external data set ===========to an external data frame
#Customer file
import numpy as np
import pandas as pd
import pandas as pd
df=pd.read_csv('C:/Users/Dell/Documents/.unknown',sep=',',header=None)
df.columns=(['id','fname','lname','age','profession','country'])
print(df)  #it has no header tag
print(df.head())
print(df.tail())
print(df.shape)

print(df.size)
print(df.describe())

#header tag absent aya filelil ==========add======> header=None

#calculate total number of missing values ============> isna().sum() ***********note note
print(df.isna().sum())

#fillna() =====> missing values has been filled by using fillna()
df1=(df.fillna('india'))
print(df1)

print(df1.isna().sum())

#how to rename columns
#newdfname=olddfname.rename(columns={'oldcolname':'newcolname'})

df1=df.rename(columns={"fname":"first_name"})
print(df1)
df2=df1.rename(columns={'id':"identity"})
print(df2)
df3=df2.rename(columns={'profession':'jooli'})
print(df3)

#iloc ==========>for finding in between values
df1=df.iloc[10:30:3]
print(df1)
df2=df.iloc[:,5:7]
df3=df.iloc[3:30,3:7]
print(df3)
print(df2)

#x seperation =====>all values except last column
#y seperation ========> it is the last column
x=df.iloc[:,:-1]
print(x)
y=df.iloc[:,-1]
print(y)

#how to collect new columns
df1=df[['fname','lname','age']]
print(df1)

#coustomer =====>fname,last name age prof
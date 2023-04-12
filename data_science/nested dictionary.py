#nested dictionary
#id fname,lname,age ,location, phno
import pandas as pd
dic={'id':[101,102,103,104,105],
     'fname':['vinay','ramu','soman','kethu','boomi'],
     'lname':['m','n','p','a','d'],
     'age':[20,21,21,22,30],
     'location':['A','B','C','D','E'],
     'Phno':[121,12123,45555,22222,9999999]}
df=pd.DataFrame(dic)
print(df)
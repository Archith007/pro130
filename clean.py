import csv 
import pandas as pd

df = pd.read_csv("merged_dataset.csv")
print(df.shape)

df.to_csv("main.csv")

df = pd.read_csv("main.csv")
print(df.shape)

del df['Unnamed: 0']
del df['Unnamed: 5']
del df['Star_name.1']
del df['Distance.1']
del df['Mass.1']
del df['Radius.1']

del df['Unnamed: 0.1']

df = df.rename({
    '':'number',
},axis = 'columns')



df.to_csv("final.csv")


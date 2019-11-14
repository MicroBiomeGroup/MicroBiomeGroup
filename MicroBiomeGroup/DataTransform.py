import pandas as pd
import numpy as np

data = pd.read_csv('GeneralData.csv',  usecols = ['Sex'])
unique, counts = np.unique(data.values, return_counts=True)
zippedDic = dict(zip(unique, counts))
myCount = sorted(zippedDic.items(), key=lambda x: x[1])
myCountAlphabetized = sorted(zippedDic.items(), key=lambda x: x[0],reverse=True)
data = pd.DataFrame(myCountAlphabetized, columns=['sex', 'count'])
data.to_csv('sex.csv', index=False)


data = pd.read_csv('GeneralData.csv',  usecols = ['Group'])
unique, counts = np.unique(data.values, return_counts=True)
zippedDic = dict(zip(unique, counts))
myCount = sorted(zippedDic.items(), key=lambda x: x[1])
myCountAlphabetized = sorted(zippedDic.items(), key=lambda x: x[0],reverse=True)
data = pd.DataFrame(myCountAlphabetized, columns=['group', 'count'])
data.to_csv('Group.csv', index=False)

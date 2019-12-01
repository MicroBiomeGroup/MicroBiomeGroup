import pandas as pd
import numpy as np
import csv
import pprint as pprint

data = pd.read_csv('GeneralData.csv',  usecols = ['Sex'])  #hh
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



with open('HeatMapBehavioralSeizures.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['group', 'variable', 'value', 'treatment'])
    with open("HeatmapSorted.csv") as f:
        f.readline() #eat the csv header from the lines
        for line in f:
            lineSplit = line.split(',')
            print(lineSplit)

            key = lineSplit[2] + " " +lineSplit[0]
            i = 4 #offset of first behavioral seizure time stamp
            hour = 1
            while(i < 16):
                value = int(lineSplit[i])
                time =  "H" + str(hour)
                hour+=1
                i+=1
                treatment = lineSplit[3]
                employee_writer.writerow([time, key, value, treatment])


with open('HeatMapFocalSeizures.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['group', 'variable', 'value', 'treatment'])
    with open("HeatmapSorted.csv") as f:
        f.readline() #eat the csv header from the lines
        for line in f:
            lineSplit = line.split(',')
            print(lineSplit)

            key = lineSplit[2] + " " +lineSplit[0]
            i = 16 #offset of first behavioral seizure time stamp
            hour = 1
            while(i < 28):
                value = int(lineSplit[i])
                time =  "H" + str(hour)
                hour+=1
                i+=1
                treatment = lineSplit[3]
                employee_writer.writerow([time, key, value, treatment])



with open('HeatMapCombinedSeizures.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['group', 'variable', 'value', 'treatment'])
    with open("HeatmapSorted.csv") as f:
        f.readline() #eat the csv header from the lines
        for line in f:
            lineSplit = line.split(',')
            print(lineSplit)

            key = lineSplit[2] + " " +lineSplit[0]
            i = 28 #offset of first behavioral seizure time stamp
            hour = 1
            while(i < 40):
                value = int(lineSplit[i])
                time =  "H" + str(hour)
                hour+=1
                i+=1
                treatment = lineSplit[3]
                employee_writer.writerow([time, key, value, treatment])

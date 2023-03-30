# Extract all files into the path specified below before running the program

path='D:\\Cyclistic\\Data\\'

import csv
import os
from datetime import datetime

filelist=[file for file in os.listdir(path) if file[-4:]=='.csv']
filelist.sort()
summary={}
for file in filelist:
    with open(path+'\\'+file,'rt') as fin:
        cin = csv.reader(fin)
        values = [row for row in cin]
    values[0].append('trip_date')
    values[0].append('trip_duration')
    for value in values[1:]:
        value.append(value[2][:-9])
        t=[]
        t.append(int(value[2][0:4]))
        t.append(int(value[2][5:7]))
        t.append(int(value[2][8:10]))
        t.append(int(value[2][11:13]))
        t.append(int(value[2][14:16]))
        t.append(int(value[2][17:]))
        t1=datetime(t[0],t[1],t[2],t[3],t[4],t[5])
        t=[]
        t.append(int(value[3][0:4]))
        t.append(int(value[3][5:7]))
        t.append(int(value[3][8:10]))
        t.append(int(value[3][11:13]))
        t.append(int(value[3][14:16]))
        t.append(int(value[3][17:]))
        t2=datetime(t[0],t[1],t[2],t[3],t[4],t[5])
        value.append((t2-t1).total_seconds())
        day=value[-2]
        if day not in summary:
            summary[day]={}
        category=value[-3]
        rideable=value[1]
        if category not in summary[day]:
            summary[day][category]={}
        if rideable not in summary[day][category]:
            summary[day][category][rideable]=[0,0]
        if value[-1]>0 and value[-1]<=86400:
            summary[day][category][rideable][0]+=1
            summary[day][category][rideable][1]+=value[-1]
    del values

summary_print=[]
summary_print.append('date')
summary_print.append('member')
summary_print.append('rideable')
summary_print.append('count')
summary_print.append('duration')
summary_print=[summary_print]
for day in summary:
    for category in summary[day]:
        for rideable in summary[day][category]:
            newrec=[]
            newrec.append(day)
            newrec.append(category)
            newrec.append(rideable)
            newrec.append(summary[day][category][rideable][0])
            newrec.append(summary[day][category][rideable][1])
            summary_print.append(newrec)

with open('D:\\Cyclistic\\summary.csv', 'wt', newline='') as filobj:
    writr = csv.writer(filobj)
    # write multiple rows
    writr.writerows(summary_print)
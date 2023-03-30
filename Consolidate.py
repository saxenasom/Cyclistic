path='D:\\Cyclistic\\Data\\'

import csv
import os
filelist=[file for file in os.listdir(path) if file[-4:]=='.csv']
filelist.sort()
with open(path+'\\'+filelist[0],'rt') as fin:
    cin = csv.reader(fin)
    values = [row for row in cin]

with open('D:\\Cyclistic\\out.csv', 'wt', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(values)

for file in filelist[1:]:
    with open(path+'\\'+file,'rt') as fin:
        cin = csv.reader(fin)
        values = [row for row in cin]
    with open('D:\\Cyclistic\\out.csv', 'at', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(values[1:])


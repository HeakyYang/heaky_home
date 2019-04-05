'''
Author:Heaky
Function:read csvfile
Version:3.7.1
Date:2019-4-5
'''

import csv
#读aapl.csv文件并打印
a=[]
with open("aapl.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print (line)
        a.append(line)
#对Volume列求和、求平均值      
sum=0
for j in range(1,len(a)):
    sum+=int(a[j][5])
ave=sum/(len(a)-1)
print(ave)

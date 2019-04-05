'''
Author:Heaky
Function:write csvfile
Version:3.7.1
Date:2019-4-5
'''
# #方法1
# import pandas as pd

# s = [1,2,3,4,5]
# a = ['mayi','jack','tom','rain','hanmeimei']
# b = [18,21,25,19,23] 
# c = [99,89,95,80,81]
# dataframe = pd.DataFrame({'NO.':s,'name':a,'age':b,'score':c})
# dataframe.to_csv("test.csv",index=False,sep=',')


#方法2
import csv

with open('test.csv','w') as csvfile: 
    writer = csv.writer(csvfile,dialect='unix')
    #先写入columns_name
    writer.writerow(['NO.','name','age','score'])
    #写入多行用writerows
    writer.writerows([[1,'maya',18,99],[2,'jack',21,89],[3,'tom',25,95],[4,'rain',19,80],[5,'hanmeimei',23,81]])


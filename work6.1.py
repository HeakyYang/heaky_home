'''
Author:Heaky
Function: write&read document
Version:3.7.1
Date:2019-4-5
'''


import random
#随机产生50个数的列表
list= []
list2=[]
for i in range(50):
    data = int(random.random()*100)
    while(data in list):
        data = int(random.random()*100)
    list.append(data)

for i in range(len(list)-1):    #从小到大排序
    for j in range(i,len(list)):
       if list[i]>list[j]:
           list[i],list[j] = list[j],list[i]
print(list)

f=open(r'D:\File\test.txt', 'w')    #创建文件&清空文件

for i in range(50):       #写入文件
    with open(r'D:\File\test.txt', 'a') as f:
        f.write(str(list[i]))
        f.write('\n')
f.close()

f = open(r'D:\File\test.txt', 'r')      #读取内容
for line in f.readlines():
    a=line.strip()
    list2.insert(0,a)

for i in range(50):       #写入文件
    with open(r'D:\File\test.txt', 'a') as f:
        f.write('\n')
        f.write(list2[i])
f.close()

    



'''
Author:Heaky
Function:score line chart2
Version:3.7.1
Date:2019-4-15
'''
import csv
import matplotlib.pyplot as plt
import numpy as np

a=[]
with open(r"F:\大三下\python\统计作业\三5.csv","r") as csvfile:     #读文件，文件目录自行更改
    reader = csv.reader(csvfile)
    for line in reader:
        # print (line)
        a.append(line)

begin_date=input("请输入起始考试日期")
end_date=input("请输入终止考试日期")
for i in range(21):
    if a[0][i]==begin_date:
        b=i
    if a[0][i]==end_date:
        e=i
ave=[]
for j in range(1,len(a)-1):
    number=a[j][0]
    name=a[j][3]
    x=[]
    x1=[]
    y=[]
    for i in range (b,e+1):
        sum=0
        n=0
        if float(a[j][i])!=0.0:     #排除没有参加考试（分数为0）的情况
            x1.append(a[0][i])
            x.append(i-4)
            y.append(float(a[j][i]))
            sum+=float(a[j][i])
            n+=1
    if n!=0:
        ave.append(sum/n)
    # else:
    #     ave.append(0)
    # print(number,x,y)
    plt.xlim(0,17)  # 限定横轴的范围
    plt.ylim(0,100)  # 限定纵轴的范围
    plt.plot(x, y,marker='o',label=r'score line')
    plt.xticks(x, x1, rotation=45)
    plt.xlabel(r"exam") #X轴标签
    plt.ylabel(r"score") #Y轴标签    
    plt.title(number) #图表标题
    plt.legend()
    plt.savefig(r"F:\大三下\python\统计作业\%s%s.jpg"%(number,name))      #保存为学号姓名，自行输入想保存的目录
    plt.clf()   #清空画布

y2=[]
for i in range(10):
    l=float(i*10)
    r=float(i*10+10)
    m=0
    for j in range(len(ave)):
        if l< ave[j] <=r:
            m+=1
        else:
            m+=0
    y2.append(m)
#print(y2)

labels = ['0+', '10+', '20+', '30+', '40+','50+','60+','70+','80+','90+']
plt.bar(range(len(y2)), y2, tick_label=labels)
plt.ylabel(r"distribution")
plt.title(r"class 5")
plt.legend()
plt.savefig(r"F:\大三下\python\统计作业\class5.jpg")


    
    
    
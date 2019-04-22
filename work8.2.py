'''
Author:Heaky
Function:Alaska temperature range
Version:3.7.1
Date:2019-4-22
'''



#encoding=utf-8  
import numpy as np
import matplotlib.pyplot as pl
from scipy import optimize

def func(x,a,b,c):
    return a*np.sin(x*np.pi/6+b)+c

month=np.linspace(1,12,12)
month1=np.linspace(1,12,120)
max =np.array([17,19,21,28,33,38,37,37,31,23,19,18])
min=[-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58]

fita,fitb=optimize.curve_fit(func,month,max,[1,1,1])
print(fita)
popt,popd=optimize.curve_fit(func,month,min,[1,1,1])
print(popt)

pl.rcParams['font.family'] = ['SimHei']
#pl.rcParams['font.sans-serif'] = ['Heiti'] # 步骤一（替换sans-serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
pl.plot(month, max, label=r"最高温") 
pl.plot(month, min, label=r"最低温")
pl.plot(month1,func(month1,fita[0],fita[1],fita[2]),label=r"最高温拟合")
pl.plot(month1,func(month1,popt[0],popt[1],popt[2]),label=r"最低温拟合")
pl.xlabel("month") #X轴标签
pl.ylabel("T") #Y轴标签    
pl.title(r"阿拉斯加温度区间") #图表标题
pl.legend()
pl.show()
'''
Author:Heaky
Function:experiment data
Version:3.7.1
Date:2019-4-22
'''



# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)+c
    """
    A, k, theta ,c = p
    return A*np.sin(2*np.pi*k*x+theta)+c   

def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)

x = np.linspace(0, 48, 17)
x1=np.linspace(0,48,200)
A, k, theta,c = 45, 0.04, -5,5 # 真实数据的函数参数
y0 = func(x, [A, k, theta,c]) # 真实数据
y1 = [48.5 ,52.6,27.0,-13.8,-38.0,-29.5,-4.9,25.2,48.6,53.2,26.7,-16.1,-39.4,-29.9,-3.5,25.2,48.5]  # 加入噪声之后的实验数据    
print(x,y0,y1)
p0 = [45, 0.030, -10,4] # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y1, x))

print("真实参数:", [A, k, theta,c] )
print("拟合参数", plsq[0]) # 实验数据拟合后的参数
pl.rcParams['font.family'] = ['SimHei']
#pl.rcParams['font.sans-serif'] = ['Heiti'] # 步骤一（替换sans-serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
pl.plot(x, y0, label=r"人为构造的真实数据")  #因为实验没有参考值/理论值（即所谓的真实数据），所以我人为构造了一组所谓的真实数据
pl.plot(x, y1, label=r"实验数据")
pl.plot(x1, func(x1, plsq[0]), label=r"拟合数据")
pl.legend()
pl.show()
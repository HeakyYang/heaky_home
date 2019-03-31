'''
Author:Heaky
Function:Dates count
Version:3.7.1
Date:2019-3-31
'''

def leap_year(y):   #判断是否是闰年
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False
        
def days_month(y, m):    #判断每个月总共有几天
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        if leap_year(y):
            return 29
        else:
            return 28
def days_year(year):   #判断今年共几天
    if leap_year(year):
        return 366
    else:
        return 365
            
def days_passed(year, month, day):  #判断今年过了几天
    m = 1
    days = 0
    while m < month:
        days += days_month(year, m)
        m += 1
    return days + day

def days_count(year1, month1, day1, year2, month2, day2):     #求两个日期之间的间隔天数
    if year1 == year2:
        return days_passed(year2, month2, day2) - days_passed(year1, month1, day1)
    else:
        s = 0
        y1 = year1
        while y1 < year2:
            s += days_year(y1)
            y1 += 1
        return s-days_passed(year1,month1,day1)+days_passed(year2,month2,day2)

date1=input("请输入起始日期：")
date2=input("请输入终止日期：")
#进行字符串的切割
startdate=date1.split(',')
enddate=date2.split(',')
print("间隔天数：",days_count(int(startdate[0]), int(startdate[1]), int(startdate[2]), int(enddate[0]), int(enddate[1]), int(enddate[2])))

    
    



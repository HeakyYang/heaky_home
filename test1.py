'''
Author:Heaky
Function:Address book management
Version:3.7.1
Date:2019-3-31
'''
func=0
tellbook = {}
while(func!=7):
    print('''菜单：
1.新增联系人
2.删除联系人
3.查询联系人 
4.显示所有联系人
5.修改联系人姓名
6.修改联系人手机
7.退出
''')
    func = int(input())
    if func ==1 :
        name=input('名字:')
        if name not in tellbook:
            tellbook[name]=input('联系电话:')
            print("添加成功")
        else:
            print("重名")
    if func == 2:
        name=input('名字:')
        if name in tellbook:
            del tellbook[name]
            print("删除成功")
        else:
            print("没有这个联系人")
    if func ==3:
        name=input('名字:')
        if name in tellbook:
            print("手机：",tellbook[name])
        else:
            print("没有这个联系人")
    if func ==4:
        print(tellbook.keys())
    if func ==5:
        name=input('名字:')
        if name in tellbook:
            print("手机：",tellbook[name])
            tellbook[name]=input("请输入修改后的手机：")
            print("修改成功")
        else:
            print("没有这个联系人")
    if func ==6:
        name=input('名字:')
        if name in tellbook:
            a=input("请输入要改成的名字：")
            tellbook[a] = tellbook.pop(name)
            print("修改成功")
        else:
            print("没有这个联系人")
print("已退出")
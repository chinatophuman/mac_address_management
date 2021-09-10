import pymysql
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

def update():
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='joinus123', db='test1')
    curson = db.cursor()
    # 获取mac起始地址
    start_address = entry1.get()
    # 获取mac终止地址
    end_address = entry2.get()
    # 获取提取人
    unit = entry3.get()
    # 获取起始和终止ID
    sql1="select * from mac_address where mac_address='%s'"%(start_address)
    curson.execute(sql1)
    result1 = curson.fetchall()
    for row1 in result1:
        global id1
        id1 = row1[0]
        int(id1)
        # print(id1)
    sql2="select * from mac_address where mac_address='%s'"%(end_address)
    curson.execute(sql2)
    result2 = curson.fetchall()
    for row2 in result2:
        global id2
        id2 = row2[0]
        int(id2)
        # print(id2)
    # 提取数据
    sql3="update mac_address set status='used',used_time=now(),user='%s' where '%d'<=id and id<='%d'"%(unit,id1,id2)
    try:
        curson.execute(sql3)
        db.commit()
        showinfo(message='数据提取成功')
    except:
        db.rollback()
        showinfo(message='失败，请确认mac地址是否有效')

    db.close()

root = Tk()
# 建立图形界面，大小1080*720
canvas1 = tk.Canvas(root, width=1080, height=720, relief='raised')
canvas1.pack()
# 图形界面里面需要显示的第一句内容，字体，颜色，位置
label1 =tk.Label(root, text='请输入要提取的mac起始地址')
label1.config(font=('Arial',22),fg=('red'))
canvas1.create_window(540, 210,window=label1)
# 增加输入框一
entry1 = tk.Entry(root)
canvas1.create_window(540, 250,window=entry1)
# 图形界面里面需要显示的第二句内容，字体，颜色，位置
label2 =tk.Label(root, text='请输入要提取的mac终止地址')
label2.config(font=('Arial',22),fg=('red'))
canvas1.create_window(540, 290,window=label2)
# 增加输入框而
entry2 = tk.Entry(root)
canvas1.create_window(540, 330,window=entry2)
# 图形界面里面需要显示的第三句内容，字体，颜色，位置
label3 =tk.Label(root, text='请输入提取人')
label3.config(font=('Arial',22),fg=('green'))
canvas1.create_window(540, 370,window=label3)
# 增加输入框三
entry3 = tk.Entry(root)
canvas1.create_window(540, 410,window=entry3)
# 增加确认按钮
button1= tk.Button(root,text='提取',command = update,bg='green',fg='red',font=('Arial','9','bold'))
canvas1.create_window(540,450,window=button1)

root.mainloop()
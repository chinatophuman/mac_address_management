import pymysql
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import csv
import time

def update():
    # 获取mac数量
    mac_number = entry1.get()
    # 获取提取人
    unit = entry2.get()
    float1=float(mac_number)
    int1=int(float1)
    if len(unit)>0:
        if int1 == float1 and int1 > 0:
            # 打开数据库连接
            db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='joinus123', db='test1')
            curson = db.cursor()


            sql1="select * from mac_address where status='free'"
            curson.execute(sql1)
            result1 = curson.fetchall()
            id1=result1[0][0]
            id2=id1+int1
            id3=int1-1
            # for row1 in result1:
            #     global id1
            #     id1 = row1[0]
            #     int(id1)
                # print(id1)
            # sql2="select * from mac_address where mac_address='%s'"%()
            # curson.execute(sql2)
            # result2 = curson.fetchall()
            # for row2 in result2:
            #     global id2
            #     id2 = row2[0]
            #     int(id2)
                # print(id2)
            # 提取数据
            sql2="update mac_address set status='used',used_time=now(),user='%s' where '%d'<=id and id<'%d'"%(unit,id1,id2)
            sql3="select * from mac_address where '%d'<=id and id<'%d'" %(id1, id2)
            sql4="select status,count(1) as count from mac_address group by status"
            try:
                curson.execute(sql2)
                curson.execute(sql3)
                data1 = curson.fetchall()
                now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
                csv_name = now + '_'+unit + '_' + mac_number + '_' + result1[0][1] + '_' + result1[id3][1] + ".csv"
                # name_total = csv_name + result1[0][1] + result1[id2-2][1]
                with open(csv_name , 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, dialect=("excel"))
                    csvwriter.writerow(["id", "mac_address", "status", "used_time", "user"])
                    for row1 in data1:
                        id = row1[0]
                        mac_address = row1[1]
                        status = row1[2]
                        used_time = row1[3]
                        user = row1[4]
                        # print(type(id))
                        # print(type(mac_address))
                        # print(type(status))
                        # print(type(used_time))
                        # print(type(user))
                        csvwriter.writerow([id, mac_address, status, used_time, user])

                db.commit()
                showinfo(message='mac地址提取成功')
            except:
                db.rollback()
                showinfo(message='提取mac地址失败')

            try:
                curson.execute(sql4)
                data2 = curson.fetchall()
                label3 =tk.Label(root, text=('剩余mac地址数量为:',data2[1][1]))
                label3.config(font=('Arial',22),fg=('green'))
                canvas1.create_window(540, 410,window=label3)
                db.commit()
            except:
                db.rollback()
                showinfo(message='统计剩余mac地址失败')

            db.close()
        else:
            showinfo(message="mac地址数量请输入整数")
    else:
        showinfo(message="请输入提取人")

root = Tk()
# 建立图形界面，大小1080*720
canvas1 = tk.Canvas(root, width=1080, height=720, relief='raised')
canvas1.pack()
# 图形界面里面需要显示的第一句内容，字体，颜色，位置
label1 =tk.Label(root, text='请输入要提取的mac地址数量')
label1.config(font=('Arial',22),fg=('red'))
canvas1.create_window(540, 210,window=label1)
# 增加输入框一
entry1 = tk.Entry(root)
canvas1.create_window(540, 250,window=entry1)
# 图形界面里面需要显示的第二句内容，字体，颜色，位置
label2 =tk.Label(root, text='请输入提取人')
label2.config(font=('Arial',22),fg=('red'))
canvas1.create_window(540, 290,window=label2)
# 增加输入框而
entry2 = tk.Entry(root)
canvas1.create_window(540, 330,window=entry2)
# 图形界面里面需要显示的第三句内容，字体，颜色，位置
# label3 =tk.Label(root, text='请输入提取时间')
# label3.config(font=('Arial',22),fg=('green'))
# canvas1.create_window(540, 370,window=label3)
# 增加输入框三
# entry3 = tk.Entry(root)
# canvas1.create_window(540, 410,window=entry3)
# 增加确认按钮
button1= tk.Button(root,text='提取',command = update,bg='green',fg='red',font=('Arial','9','bold'))
canvas1.create_window(540,370,window=button1)

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='joinus123', db='test1')
curson = db.cursor()

sql5="select status,count(1) as count from mac_address group by status"
curson.execute(sql5)
result2 = curson.fetchall()
if len(result2)>1:
    rest = int(result2[1][1])
    if rest < 20000:
        label4 =tk.Label(root, text=('mac地址余量不足，剩余mac地址数量为',rest))
        label4.config(font=('Arial',22,'bold'),fg=('red'))
        canvas1.create_window(540, 100,window=label4)

db.close()

root.mainloop()


import pymysql
from tkinter.messagebox import showinfo


db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='joinus123', db='test1')
curson = db.cursor()

sql1="select status,count(1) as count from mac_address group by status"
curson.execute(sql1)
result1 = curson.fetchall()
print(len(result1))
# print(result1)
# print(result1[0])
# print(result1[1][1])
# a=result1[0]
# for row1 in result1:
#     id1 = row1[0]
#     print(id1)

db.close()
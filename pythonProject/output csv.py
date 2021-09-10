import csv
import pymysql
import time


db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='joinus123', db='test1')
curson = db.cursor()

sql1="select * from mac_address where status='free'"
curson.execute(sql1)
data = curson.fetchall()
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
name = now + '_' + 'Qzh' + '_'+ '3'
with open(name,'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile,dialect=("excel"))
    csvwriter.writerow(["id","mac_address","status","used_time","user"])
    for row2 in data:
        id = row2[0]
        mac_address = row2[1]
        status = row2[2]
        used_time = row2[3]
        user = row2[4]
        # print(type(id))
        # print(type(mac_address))
        # print(type(status))
        # print(type(used_time))
        # print(type(user))
        csvwriter.writerow([id,mac_address,status,used_time,user])

db.close()
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='joinus123',db='test1')
cur = conn.cursor()

# 创建数据表mac_address
cur.execute('drop table if exists mac_address')
sql= """create table mac_address(
        id int auto_increment primary key unique,
        mac_address char(20) unique null,
        status char(20) null,
        used_time char(20) null,
        user char(20) null)"""
cur.execute(sql)

#关闭数据库连接
cur.close()
conn.close()
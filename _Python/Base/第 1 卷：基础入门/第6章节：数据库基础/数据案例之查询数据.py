# 查询数据
import mysql.connector
conn = mysql.connector.connect(user='root', password='Liyanxia802.', database='members')

cursor = conn.cursor()
cursor.execute('select * from userInfo')

var = cursor.fetchall()  # fetchall 获取所有（data）

# print(var)
for i in var:
    print(i)

cursor.close()
conn.close()

# 会员系统
"""
1.构建数据库
    知识点：sql语句
    操作： MySQL客户端
    create database数据库
    查看数据库
    查看表

2.构建表
    知识点：python语法
    实现： MySQL + python 学习
    导入、连接
    构建表、插入数据
    提交数据、关闭表

3.查询数据
    知识点： python语法
    实现： python 学习 + sql
    导入库、连接
    查询表
    显示、关闭
"""
import mysql.connector

conn = mysql.connector.connect(user='root', password='Liyanxia802.', database='members')
# members 会员
# connect 连接
# cursor 光标
cursor = conn.cursor()
cursor.execute('create table userInfo (\
    ID varchar(20) primary key, \
    name varchar(20))')  # 生成用户信息表,ID,Name两个字段

cursor.execute('insert into userInfo (ID,name) values (%s,%s)', ['001', '张三'])
cursor.execute('insert into userInfo (ID,name) values (%s,%s)', ['002', '李四'])
cursor.execute('insert into userInfo (ID,name) values (%s,%s)', ['003', '王五'])
# insert 嵌入
# %s占位，可用作print的格式化输出：打印字符串
conn.commit()  # commit 提交
cursor.close()
conn.close()

# 查询数据
# select * from [table_name];  查看表的所有内容

"""
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
"""

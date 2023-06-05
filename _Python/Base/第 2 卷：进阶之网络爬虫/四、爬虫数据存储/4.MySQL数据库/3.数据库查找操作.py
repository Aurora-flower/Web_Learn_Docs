#!/usr/bin/env python3

"""
# @Create   : 2022/6/28  15:53
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   15:53       Software Name          1.0.0
"""
import pymysql

# 查找数据
"""
使用pymysql查询数据，可以使用fetch*方法：
    1. fetchone():  可以每次获取一条数据
    2. fetchall():  可以接受全部的返回结果
    3. fetchmany(size): 可以获取指定条数的数据
"""

# 数据库链接操作
database_connect =pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="Liyanxia802.",
                                  database="csdn")

# 光标对象
cursor = database_connect.cursor()

# 执行语句
cursor.execute("select * from article where id<3")    # where id<3：表示选择id<3的数据

# 提取数据
# result = cursor.fetchone()
result = cursor.fetchall()
# result = cursor.fetchmany(17)

# 打印结果
print(result)

# 关闭数据库
cursor.close()
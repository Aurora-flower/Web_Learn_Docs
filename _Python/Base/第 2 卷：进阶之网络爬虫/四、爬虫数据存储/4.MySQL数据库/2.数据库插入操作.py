#!/usr/bin/env python3

"""
# @Create   : 2022/6/28  15:36
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   15:36       Software Name          1.0.0
"""

# 语法格式：
#   insert into [表名(字段)] values(字段对应的值)

import pymysql

# 连接数据库
database_test = pymysql.connect(host="localhost",
                                user='root',
                                password='Liyanxia802.',
                                database='csdn',
                                port=3306
                                )

# 定义数据库语句(设置了自动增长，id设为null)
sql_statement = "insert into article(id,title,content)values(null,'x','y');"

# 在数据不能保证的情况下，可以使用以下方式：
'''
如果值是动态变化的，那么可以使用`%s`来先作为指代，后期在使用execute方法的时候，可以给一个元组把这些数据填补。
sql_statement = "insert into user([字段])values(null,%s);"
cursor.execute(sql_statement,([指定字段数据]))
'''
# 光标对象
cursor = database_test.cursor()

# 执行语句
cursor.execute(sql_statement)

# 提交
database_test.commit()

# 关闭数据库
database_test.close()

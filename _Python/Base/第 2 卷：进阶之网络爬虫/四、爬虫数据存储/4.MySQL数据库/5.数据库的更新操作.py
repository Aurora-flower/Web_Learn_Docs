#!/usr/bin/env python3

"""
# @Create   : 2022/6/28  16:14
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   16:14       Software Name          1.0.0
"""

# 更新语句：         (升级 upgrade)
#   update [form_name] set [字段='字符串' where id=数字]

import pymysql

# 连接数据库
data_conn = pymysql.connect(user='root',
                            host="localhost",
                            port=3306,
                            password="Liyanxia802.",
                            database="csdn",
                            )

# 标记对象
cursor = data_conn.cursor()

# 定义语句
sentence = "update article set title='钢铁是怎样炼成的',content='自信，自强，但不自负' where id=3"

# 执行语句
cursor.execute(sentence)

# 提交操作
data_conn.commit()

# 关闭数据库
data_conn.close()
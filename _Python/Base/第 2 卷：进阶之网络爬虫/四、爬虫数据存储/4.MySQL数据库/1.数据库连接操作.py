#!/usr/bin/env python3

"""
# @Create   : 2022/6/22 18:24
# @Author   : 30945
# @Description  :   python 学习 连接 mysql操作
@Date Time         @Version
------------      -------------  
2022/6/22 18:24      1.0.0
"""

# 使用 pymysql.connect 方法链接数据库
import pymysql

# 连接数据库
database_test = pymysql.connect(host="localhost",
                                user='root',
                                password='Liyanxia802.',
                                database='csdn',
                                port=3306
                                )
"""
    * host：以后在连接外网服务器的时候，就要改成外网服务器的ip地址。
    * port：在外网一般会更换端口号，不会为3306，这是为了安全考虑。
    * user：连接的用户，一般在生产环境中会单独分配一个账号给你，而不是使用root用户。
    * password：这个用户的密码。
    * database：要连接操作的数据库名。
    * charset：设置为utf8这样就能操作中文了。
"""

# 光标对象
cursor = database_test.cursor()

# 执行语句
cursor.execute("select * from article")  # 从表格中查找所有字段
result = cursor.fetchone()  # fetch 取，获取； fetchone获取一个

# 打印结果
print(result)

# 关闭数据库
database_test.close()

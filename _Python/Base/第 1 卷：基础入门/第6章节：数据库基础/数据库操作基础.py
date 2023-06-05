# 生成数据库、表
"""
步骤：
# 后面分号" ; "不可省略
[生成数据库]
    启动-输入密码-进入-生成数据库-显示数据库-查看表
        启动：
            打开 MySQL命令行客户端
                ————MySQL 8.0 command line client-Unicode
            输入password密码
        构建数据库：
            create database [name];
            检查是否生成 show databases;
        进入数据库：
            use [name];
        查看表：
            show tables;
        查看(所有)数据：
            select * from 表名;


[生成表]
    生成表-显示表
    create table table_name (column_name column_type);      # column 列
            例：
                mysql> CREATE TABLE test(
                -> test_id INT NOT NULL AUTO_INCREMENT,   # AUTO_INCREMENT  自动增加
                -> test_title VARCHAR(100) NOT NULL,
                -> test_author VARCHAR(40) NOT NULL,
                -> submission_date DATE,            # submission 提交
                -> PRIMARY KEY ( test_id )
                -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;     # DEFAULT 违约,默认；系统默认值
                # 在C语言中，default的作用就是switch语句里所有的case都不成立时所要执行的语句。
                # ENGINE 设置存储引擎，CHARSET 设置编码。

[查看用户名]
    select user,host from mysql.user;
"""
# 构建 lesson表
import mysql.connector

# connect 连接
conn = mysql.connector.connect(user='root', password='Liyanxia802.', database='yanbin')

# cursor 光标
cursor = conn.cursor()

# 执行 mysql语句
cursor.execute('create table hello (\
    ID varchar(20) primary key, \
    name varchar(20))')
#       execute 执行
#       create 创建，创造
#       primary 基本的，主要的，初级的
"""
VARCHAR (M)是一种比 CHAR 更加灵活的 数据类型,同样用于表示字符数据，但是VARCHAR可以保存可变长度的字符串。 
其中M代表该数据类型所允许保存的字符串的最大长度，只要长度小于该最大值的字符串都可以被保存在该数据类型中。
"""

# 关闭光标对象和链接
cursor.close()
conn.close()

# -------------------------------------------
# DROP 降落，放弃；
# EXISTS 存在

# 数据库的删除
#   DROP DATABASE [IF EXISTS] 数据库名;   drop database [if exists]  [name]

# 表的删除
#   DROP TABLE [IF EXISTS] 表名;    drop table [if exists]  [name]

# 与 CREATE DATABASE语句类似，
# IF EXISTS是该语句的可选部分，以防止您删除数据库服务器中不存在的数据库、表格时发生错误。

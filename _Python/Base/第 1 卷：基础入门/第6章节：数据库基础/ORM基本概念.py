# MVC思想
# model 实体 ————  view 视图 ————  controller 控制器

# ORM  对象关系映射
#   Object Relational Mapping 把关系数据库的表映射到对象上
#   使用sqlalchemy模块

# ----------------------------------------
#     构造数据库  MySQL操作
#     插入数据    python语句
#     查询数据     python语句
"""
# 构造数据库
                    [name] 表示是数据库、表名称
create database [data_name];            生成数据库
show databases;                         查看数据库
use [data_name];                        进入数据库
    create table table_name](           构建表
    id varchar(20) primary key;         id字段
    name varchar(20),                   name字段
    ms int);                            ms字段(math score)
show tables;                            查看表
select * from [table_name];             查看表的所有内容
"""
# MySQL中，查询数据
# select * from [table_name];  查看表的所有内容




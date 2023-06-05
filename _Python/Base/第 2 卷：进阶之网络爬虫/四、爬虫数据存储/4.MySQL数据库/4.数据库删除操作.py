#!/usr/bin/env python3

"""
# @Create   : 2022/6/28  16:07
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   16:07       Software Name          1.0.0
"""

import mysql
import pymysql

"""
mysql的删除语句：
  1.数据库的删除： drop database [if exists]  [name]
  2.表的删除：    drop table [if exists]  [name]

删除指定id的数据：  
delete from [form_name] where id=数字
 
"""

# 注:更改数据库数据的操作，需要进行提交

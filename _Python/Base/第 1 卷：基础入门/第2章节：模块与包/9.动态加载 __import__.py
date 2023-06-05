# __import__() 函数用于动态加载类和函数 。
#   如果一个模块经常变化就可以使用 __import__() 来动态载入。
# 语法：
#   __import__(name[, globals[, locals[, fromlist[, level]]]])

# 参数说明：
# name -- 模块名
# globals -- 全局变量；全局
# locals -- 当地的
# form-list -- 表格-列表
# level -- 水平，品质

# -----------------------------------------------------------------------------------------------------

import sys

__import__('mode')  # 导入 mode.py 模块




# remark
"""
# @Create   : 2022/6/28  17:27
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   17:27       Software Name          1.0.0
"""

import time


def coding():
    for x in range(3):
        print("%d正在写代码..." % x)
        time.sleep(1)


def drawing():
    for x in range(3):
        print("%d正在画图..." % x)
        time.sleep(1)


def main():
    coding()
    drawing()


if __name__ == '__main__':
    main()

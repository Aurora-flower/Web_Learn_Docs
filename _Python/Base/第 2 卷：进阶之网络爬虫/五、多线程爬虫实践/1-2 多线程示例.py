"""
# @Create   : 2022/6/28  17:27
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   17:27       Software Name          1.0.0
"""

import time
import threading


def code():
    for x in range(3):
        print("%d正在写代码..." % x)
        time.sleep(1)


def draw():
    for x in range(3):
        print("%d正在画图..." % x)
        time.sleep(1)


def single_thread():
    code()
    draw()


def multi_thread():
    th1 = threading.Thread(target=code)
    th2 = threading.Thread(target=draw())

    th1.start()
    th2.start()


if __name__ == '__main__':
    # single_thread()
    multi_thread()

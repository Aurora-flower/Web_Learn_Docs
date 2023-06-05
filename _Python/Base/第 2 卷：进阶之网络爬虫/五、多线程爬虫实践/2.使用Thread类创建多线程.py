"""
# @Create   : 2022/6/28  17:17
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   17:17       Software Name          1.0.0
"""

#  -----------------------------------------------------------------------------
import time
import threading

# 两个小知识点：
#   1. 使用 threading.current_thread()可以看到当前线程的信息。    current 当前，目前
#   2. 使用threading.enumerate()函数便可以看到当前的线程


#  -----------------------------------------------------------------------------
# 继承自 threading.Thread类
"""
    为了让线程代码更好的封装。可以使用threading模块下的Thread类，继承自这个类，然后实现
run方法，线程就会自动运行run方法中的代码。
"""
# 优点： 类可以更加方便的管理，使用面向对象的方式进行编程。

class CodingThread(threading.Thread):
    def run(self):
        # thread对象
        the_thread = threading.current_thread()
        for x in range(3):
            print("%s正在写代码..." % the_thread.name)
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        the_thread = threading.current_thread()
        for x in range(3):
            print("%s正在画图..." % the_thread.name)
            time.sleep(1)


# 多线程
def multi_thread():
    th1 = CodingThread(name='小红')
    th2 = DrawingThread(name='小明')

    # 开始进程
    th1.start()
    th2.start()


if __name__ == '__main__':
    multi_thread()

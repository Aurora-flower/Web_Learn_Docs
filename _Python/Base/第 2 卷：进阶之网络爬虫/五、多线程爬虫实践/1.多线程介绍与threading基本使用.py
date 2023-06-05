"""
# @Create   : 2022/6/28  17:11
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/28   17:11       Software Name          1.0.0
"""
#  -----------------------------------------------------------------------------
# IO编程
import threading

"""
    IO在计算机中指的是Input/Output，也就是输入输出。
    凡是用到数据交换的地方，都会涉及IO编程，例如磁盘、网络的数据传输。
    在IO编程中，Stream（流）是一种重要的概念，分为输入流（Input Stream）和输出流（Output Stream）。
"""

# 多线程：
"""
    多线程（multithreading），是指从软件或者硬件上实现多个线程并发执行的技术。
    具有多线程能力的计算机因有硬件支持而能够在同一时间执行多于一个线程，进而提升整体处理性能。
    具有这种能力的系统包括对称多处理机、多核心处理器以及芯片级多处理或同时多线程处理器。
    在一个程序中，这些独立运行的程序片段叫作“线程”（Thread），利用它编程的概念就叫作“多线程处理”.
"""

# 理解：
#   默认情况下，一个程序只有一个进程和一个线程，代码是依次线性执行的。
#   而多线程则可以并发执行，一次性多个人做多件事，自然比单线程更快。

'''
threading模块是python中专门提供用来做多线程编程的模块。
threading模块中最常用的类是Thread。
'''
threading.Thread()      #  target 目标

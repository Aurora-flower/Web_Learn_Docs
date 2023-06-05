#!/usr/bin/env python3
# coding=utf-8

"""
# @Create   : 2022/6/30  16:32
# @Author   : 30945  HuaYin
# @Description  :   说明文件功能
@Date Time              @Software              @Version
-----------------      ----------------        -------------
2022/6/30   16:32       Software Name          1.0.0
"""

#  -----------------------------------------------------------------------------
# 生产者和消费者模式
#       生产者 -> 中间容器 -> 消费者
import threading
import random

"""
    生产者和消费者模式是多线程开发中经常见到的一种模式。
    生产者的线程专门用来生产一些数据，然后存放到一个中间的变量中。消费者再从这个中间的变量中
取出数据进行消费。
    通过生产者和消费者模式，可以让代码达到高内聚低耦合的目标，程序分工更加明确，线程更加方便管理.
"""

# 高内聚低耦合
"""
    高内聚低耦合，是[软件工程]中的概念，是判断软件设计好坏的标准，主要用于程序的面向对象的设计，
主要看类的内聚性是否高，耦合度是否低. 
    目的是使程序模块的可重用性、移植性大大增强. 
    通常程序结构中各模块的内聚程度越高，模块间的耦合程度就越低. 
    内聚是从功能角度来度量模块内的联系，一个好的内聚模块应当恰好做一件事，它描述的是模块内的功能联
系；耦合是软件结构中各模块之间相互连接的一种度量，耦合强弱取决于模块间接口的复杂程度、进入或访问一
个模块的点以及通过接口的数据。
"""

#  -----------------------------------------------------------------------------
# Lock版的生产者和消费者模式
gMoney = 0
gTimes = 0
gLock = threading.Lock()


# 生产者
class Producer(threading.Thread):
    def run(self) -> None:  # 表示返回值为 None
        global gMoney
        global gTimes
        while True:  # 通过while True死循环并且上锁
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()  # 有始有终
                break
            money = random.randint(0, 100)
            gMoney += money
            gTimes += 1
            print("%s生产了%d元钱" % (threading.current_thread().name, money))
            gLock.release()

    #     pass


# 消费者
class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            gLock.acquire()
            money = random.randint(0, 100)
            if gMoney >= money and gTimes:
                gMoney -= money
                gTimes += 1
                print("%s消费了%d元钱" % (threading.current_thread().name, money))
            else:
                if gTimes >= 10:
                    gLock.release()
                    break
                print("%s想要消费了%d元钱,但是余额只有%d" % (threading.current_thread().name, money, gMoney))
            gLock.release()
    #     pass


def main():
    # th1 = threading.Thread(target=Producer)
    # th2 = threading.Thread(target=Consumer)
    # 生产者线程
    for x in range(1):
        th1 = Producer(name="生产者%d号" % x)
        th1.start()
    # 消费者线程
    for y in range(1):
        th2 = Consumer(name="消费者%d号" % y)
        th2.start()


if __name__ == '__main__':
    main()

#  -----------------------------------------------------------------------------
# Condition版的生产者和消费者模式
"""
    Lock版本的生产者与消费者模式可以正常的运行。但是存在一个不足，在消费者中，总是通过while True
死循环并且上锁的方式去判断钱够不够。上锁是一个很耗费CPU资源的行为,因此这种方式不是最好的。
    更好的方式便是使用threading.Condition来实现,threading.Condition可以在没有数据的时候处于
阻塞等待状态。一旦有合适的数据了，还可以使用notify相关的函数来通知其他处于等待状态的线程。这样就可以不用
做一些无用的上锁和解锁的操作,可以提高程序的性能。
    threading.Condition类似threading.Lock，可以在修改全局数据的时候进行上锁，也可以在修改完毕后进行
解锁。
1. acquire：上锁。
2. release：解锁。
3. wait：将当前线程处于等待状态，并且会释放锁。可以被其他线程使用notify和notify_all函数唤醒。被唤
醒后会继续等待上锁，上锁后继续执行下面的代码。
4. notify：通知某个正在等待的线程，默认是第1个等待的线程。
5. notify_all：通知所有正在等待的线程。notify和notify_all不会释放锁。并且需要在release之前调用.
"""

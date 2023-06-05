# o'clock (of the clock) 点钟
import time

"""
程序设计时常需要时间信息.
    * time()          可以回传自 1970 年 1 月 1 日 00:00:00 AM 以来的秒数 
    * sleep(n sec)    可以让工作暂停 n 秒
    * asctime()       列出可以阅读的目前系统时间
    * localtime()     可以返回目前的时间的结构数据
    * ctime()         与localtime()相同,不过返回的是字符串
    * clock()         取得程序执行的时间(旧版，不建议使用)
    * process_time()  取得程序执行的时间(新版)
"""

# ----------------------------------------------------------------------------------------------------------
# time.time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）,返回值是秒
'''
    初看是没有什么用处。如果想要掌握某段工作所花费的时间是很有用的。
'''
start = time.time()  # start 开始； end 结束

count = 0
while count < 3:
    count += 1
    print(f"距离结束{2 - count}secs")
    time.sleep(1)
    print(f"花费时间{time.process_time()}")

end = time.time()
print("工作时间为：%s" % (end - start))

# ----------------------------------------------------------------------------------------------------------
# time.localtime()函数类似 gm-time()，作用是格式化时间戳为本地的时间。如果 sec参数未输入，则以当前时间为转换标准。
"""
struct_time元组共有9个元素：
    * tm_year(年）
    * tm_mon(月）
    * tm_mday(日)
    * tm_hour(时)
    * tm_min(分)  minute 分钟
    * tm_sec(秒) 
    * tm_wday(weekday)    0是周一，一次类推
    * tm_yday(一年中的第几天)
"""
print(time.localtime())
print(time.ctime())
print(time.asctime())  # 列出可以阅读的目前系统时间
# ----------------------------------------------------------------------------------------------------------
# Python 编程中使用 time 模块可以让程序休眠，具体方法是 time.sleep (秒数)，其中”秒数”以秒为单位，
# 可以是小数，0.1秒则代表休眠 100毫秒.   1 sec = 1000 ms    (millisecond)
"""
短暂停止：
import time
time.sleep(sec)     second 秒；第二（的）
time.localtime()        当地时间
"""

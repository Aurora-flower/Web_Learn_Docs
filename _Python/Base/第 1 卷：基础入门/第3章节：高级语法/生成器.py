import sys  # system 系统
import time

# return 返回值； yield 生成器

time_one = time.time()
mylist = [i for i in range(10000000)]
time_two = time.time()
print('占用时间:', time_two - time_one)
print('占用空间:', sys.getsizeof(mylist))

time_three = time.time()
mygen = (i for i in range(10000000))

time_four = time.time()
# One, two, three, four, five, six, seven, eight, nine, ten
print('占用空间:', time_four - time_three)
print('占用空间:', sys.getsizeof(mygen))
"""
def gen(x):  # generate 生成;generators 生成器
    for variable in range(x):
        yield variable ** variable    # yield 产量，收益


generate = gen(5)
for var in generate:
    print(var, end=',')
"""

gen = (a*a for a in range(5))  # 简化版
for i in gen:
    print(i, end=' ')

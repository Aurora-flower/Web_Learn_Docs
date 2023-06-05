# 可迭代对象 iterable object

for var in {1, 2, 3}:
    print("hello")
"""
for-in 遍历循环：
格式：【 for 变量 in 集合：
         具体操作 】
   是针对可迭代对象（集合），
   循环的次数，取决于迭代集合的大小
"""
dic_var = {1, 2, 4}
for value in dic_var:  # ”in“后，是迭代对象： 列表，字典， 字符串。（元组，特殊的列表）
    print(value)  # 遍历得到的每一个值打印出来

# --------------------------------------------------
# enumerate() 枚举函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#   格式：enumerate(sequence, [start=0])
# 参数：
#   sequence -- 一个序列、迭代器或其他支持迭代对象。
#   start -- 下标起始位置的值。
'''
同时遍历索引以及它的值:
for index,name in enumerate(x):
     print(index,name)   # (a,b)
index  (物价和工资等的)指数；指标；索引；标志；表征；量度；  （第一个数是计数值）
enumerate  列举；枚举            （第二个数是元素值）
'''

# 遍历列表
str_list = ['python 学习 ', '人工智能', '大数据']
for left, right in enumerate(str_list):
    print(left, right)

# 遍历元组，元组不可变！
tuple_var = ('python 学习 ', '人工智能', '大数据')
for left, right in enumerate(tuple_var):
    print(left, right)

# ------------------------------------------------------------
'''
遍历字典：
items(): 返回字典内的 key-value 键值对
keys(): 返回字典内所有 key 列表
values(): 返回字典内所有 value 列表 
'''
dic_customize = {
    "距离升本还有": 25,
    "现有存款": 3459,
    "第一阶段目标": 10000,
}
for left, right in dic_customize.items():
    print(left, right)

for var in dic_customize.keys():  # 这里的keys可以看做是函数，而不是对象；
    print(var)

for var in dic_customize.values():
    print(var)

# ------------------------------------------------------------
# 遍历字符串
string = "我要 在CSDN 学习 python 学习"
for define in string:
    print(define, end='')  # 结果：每一个字符输出后都加连接符
'''
print(a)  # 打印结果默认是换行的;
print(a, sep='',end=" ")   # 可以是空格，也可以是其他的符号; 
'''
print('\n')

# ------------------------------------------------------------
# for-in次数控制
'''
range函数：
格式：  [ range(初始值,终止值,步长） ]
可以指定初始值、终止值以及步长。产生一个等差序列（也为可迭代对象或range对象）

'''
e = range(10)  # 生成可迭代对象（类型对象）；默认开始值是0，步长为1；不包含结束值。
# print(e)
u = list(e)  # 把可迭代对象转化为一个列表；
print(u)

# -------------------------------
'''
计算执行次数：
(a + step * 2) /n  + 1
'''
for g in range(3, 19, 2):  # step 步长
    print(g, end=",")  # 控制结尾符号
    print('hello' + '!')  # 也可以写成  print(g, 'hello') ,结果相同。

print('执行次数为：', len(range(2, 10, 2)))  # 计算执行的次数

# ------------------------------------------------------------
# 计算1到100的和
'''想法：等差数列之和
高斯算法： (首项 + 末项)* 项数 / 2  ;
项数的计算方法：(末项 - 首项) / 项差 + 1
'''
# box = 0
# for i in range(1, 101):  # 1到100，等差为1的数,循环方法
#     box += 1
#     print(box)

# 使用函数sum的方式计算1至100的和。
print(sum(range(1, 101)))  # sum 总和；归纳;总计;总结，概括

# -------------------------------
# 计算1到100内所有的奇数
p = range(1, 100, 2)
# print(list(p))
print('1到100内所有的奇数的和：', sum(list(p)))

# -------------------------------
# 通过控制起始值与步长的方式实现
# for p1 in range(1, 100, 2):
#     print(p1)

# -------------------------------
# 选择结构嵌套在循环结构内实现；
# 嵌套循环：
#   以一个循环内有另一个循环，我们称这是嵌套循环。循环的次数为[外循环 n次 * 内循环 m次]
# for p2 in range(1, 100):
#     if p2 % 2 == 1:  # 单个等号是赋值，两个等号是比较（关系）;
#         print(p2, end=',')

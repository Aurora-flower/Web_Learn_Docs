# 随机 random ,边缘 rand
#   rand (兰德) 芳香之树，平常作为女性男性英文名都可以，来源于英语，这个名字寓意独立，勇敢，有信心，有创造力。

import random

"""
    所谓的随机数是指平均散布在某区间的数字。
"""

# -----------------------------------------------------------------------------------------------------
"""
整数：
    * randrange(start,stop,step)   # 范围内，随机一个数   
    * randint(a,b)   # 产生 [x,y]的随机函数

序列：
    * choice(seq)   # 选择
    * shuffle(seq)    # 将序列的所有元素随机排序，参数random已经弃用.。
    * sample(list, number )     # 取样

实数值：
    * random()   # 随机数
    * uniform(parameter-number, argument-number)  # 随机浮点数
"""
# -----------------------------------------------------------------------------------------------------
# randint(x,y) 随机产生指定区间[x,y]的整数
n = 3
for i in range(n):
    print(f"1-100  :{random.randint(1, 100)}")

# randrange() 范围内，随机一个数
print(random.randrange(0, 100, 5))  # 格式： [star,end,step]

# -----------------------------------------------------------------------------------------------------
# choice() 对象中随机选择一个
string = ["apple", "orange", "banana"]
print(random.choice(string))  # 参数 seq --可以是一个列表，元组或字符串

# range() 返回的是一个可迭代对象（类型是对象），而不是列表类型
variable = range(10)  # range(start, stop[, step])/range(object)
print(list(variable))
parameter = range(15)  # parameter 参数
print(list(parameter))
seq = list(parameter)
# shuffle() 方法将序列的所有元素随机排序
# random.shuffle(seq)     # 返回值是个 None，操作的对象是一个list
print(f"是否有返回值{random.shuffle(seq)}")  # 结论：该函数没有返回值。
print(f"是否有返回值{seq}")
print(type(seq))

# sample() 样本
#   语法：sample(列表,数量)
lst = ["character string", "alphabetic string", "字符串"]
var = random.sample(lst, 1)  # 第 2个是位置参数(positional arguments )，最大不能超过规模值
print(var)
print(type(var))

# -----------------------------------------------------------------------------------------------------
# uniform() 均匀
print(random.random())  # 返回一个 [0,1] 之间的随机浮点数
print(random.uniform(3.14, 3.15))  # 设置参数值 a,b，返回一个[a,b]之间随机浮点数

# -----------------------------------------------------------------------------------------------------
# 作业：

# 1,生成一个在 100到 200之间的随机偶数
numbers = random.randrange(100, 200, 2)
print(numbers)

# 2.将 1到 100之间数字随机排列
name = range(1, 101)
rand = list(name)
print(rand)
random.shuffle(rand)  # 打乱次序
print(rand)

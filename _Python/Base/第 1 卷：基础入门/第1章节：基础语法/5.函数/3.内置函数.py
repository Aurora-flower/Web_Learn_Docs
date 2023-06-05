# 内置函数
# dir()函数
#   可以列出所有的内置函数
"""
builtins = dir(__builtins__)        # builtins 内置
for i in builtins:
    print(f">>>{i}", end=';\n')
"""

# help()函数查看function功能

# 元素除了是 0、空、None、False 外都是 True
# 空元组、空列表返回值为 True


# 内置函数 dict()建立字典
a = dict(距离升本=28, 已经存款=3400)  # dict 构造字典（生成，定义）
print(a)

# --------------------------------------------------------------------
variable = [1, 15, 64, 48, 94, 8, 9, 78, 8, 97, 89, 7, 89, 7]
print(max(variable))  # maximum 最大值
print(min(variable))  # minimum 最小值
print(sum(variable))  # 求和(数值型数据)
print(pow(2, 3))  # 幂函数， pow([base，exp，mod])   base 基础； exponent 指数，幂；mod 求余

# --------------------------------------------------------------------

"""
num = [(1,2.5), (1.5, 3.2), (1.3, 4.0), (2.2, 1.8)]

# 相当于找4组坐标的第1个数的最大值，显然为2.2
y,z = max(num, key=lambda x:x[0])
print(y, z)
"""
dic = {
    "距离升本还有": 18,
    "存款": 3450,
}
# 格式:
#   max/min (key=lambda 元素: 元素[字段索引])
print(max(dic, key=lambda h: dic[h]))  # 隐函数 lambda

# --------------------------------------------------------------------
# sorted 函数
#   对所有的可迭代对象进行排序操作，保持原对象不变；
'''
sorted(__iterable,key,reverse)
iterable: 可迭代对象
reverse: 颠倒，相反的
'''
print(sorted(variable))
object_var = sorted(variable, reverse=True)
print(object_var)

# --------------------------------------------------------------------
# zip()函数
#   用于将可迭代对象作为参数，将对象对应的元素打包成一个个元组，然后返回这些元组组成的列表。
a = [4, 59, 5, 97, 89]
b = [19, 87, 36, 1, 50]
ab = zip(a, b)
print(ab)
print(list(ab))

# iterate 迭代(数学或计算过程，或一系列指令)

# --------------------------------------------------------------------
# all()函数
#   用于判断给定的可迭代参数 iterable(可迭代的)中，
#   所有的元素是否为 True，如果是返回 True；否则返回 False
print(all([3, None, 4, 44, 87, 8, 4, 7, 84, 54]))
x = []
print(all(x))

# ------------------------------------
# any()函数
#   用于判断给定的可迭代参数 iterable 中，
#   全部为 False，则返回 False；
#   如果有一个 True，则返回 True
#   空元组、空列表返回值为 False
print(any([0, 0, 0, 0, 1, 0]))
print(any(x))

# --------------------------------------------------------------------
# 作业：介绍常用的内置函数，并给出示范程序；

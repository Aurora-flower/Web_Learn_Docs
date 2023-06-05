"""
集合：
    集合的基本观念是无序且每个元素唯一的值。
    集合元素的内容是不可变的(immutable)：
        常见的元素有整数(integer)、浮点数(float)、字符串(string)、元组(tuple);
    至于可变(mutable)内容：
        列表(list)、字典(dictionary)、集合(set)等不可以是集合元素。
    集合是无序的不重复元素序列，重复元素会被自动去掉;但其本身是可变的。
"""

# copy复制，paste 粘贴
# --------------------------------------------------------------------
# 建立集合（大括号）

# 大括号建立
x = {243, 45, 566, 69}  # 集合 set中，无重复的元素，且无序!

# set()函数定义
#   内置函数，有设置、集合的意思。将列表、元组等迭代对象（或字符串）转换为集合
x1 = [238, 5, 79, 90, 25]
x2 = (8, 6, 7, 7, 9)
print(set(x1))
print(set(x2))

# --------------------------------------------------------------------
# 给集合添加元素[ set-name.add(element) ],element 元素
x.add(633)
print(x)

# --------------------------------------------------------------------
# 删除集合， [ del set-name ]
del x  # 此时打印输出集合x,则是没有 defined（定义）

# --------------------------------------------------------------------
# 随机删除集合中的一个元素， [ set-name.pop() ]
x3 = set(x1)
x3.pop()
print(x3)

# --------------------------------------------------------------------
# 删除集合中的指定元素， [ set-name.remove(element) ]
x3.remove(90)  # remove 去除，移开，拿开
print(x3)  # 可以发现：这里的输出结果，是在上一次输出结果的基础上作的改动

# discard()
#       可以删除集合的元素，如果元素不存在也不会出错
#   [ret_value = 集合A.discard(欲删除的元素)]
#       无论是否删除结果如何，该方法都会返回 None（在一些语言中也是 NULL）
set_diss = {1, 5, 9}
set_diss.discard(1)
print(set_diss)

# --------------------------------------------------------------------
# 删除集合中所有的元素，   [ set-name.clear() ]
x3.clear()  # clear 清楚，清理；干净的
print(x3)

# --------------------------------------------------------------------
# 作业：实现集合间的并、交、差操作
# 格式[ set-name1.function(set2,set3) ]

# 并集union，
# 交集（相交/交点）intersection，
# 差集（不同/差异）difference

# -------------------------------------
# 集合的操作运算符号：
"""
&               交集(相交/交点,intersection)
!               并集(union)
-               差集(不同/差异,difference)
^               对称差集（symmetric difference）
==              等于
!=              不等于
in              成员
not in          非成员
"""

# 对称差集合
#   排除同时属于 A集合和 B集合的元素
set_sym_one = {1, 2, 3, 4}
set_sym_two = {4, 5, 6, 7}
set_twice = set_sym_one ^ set_sym_two
print("对称差集=", set_twice)

# in成员
boolean = 1 in set_sym_one
print(boolean)

# not in成员
boolean = 1 not in set_sym_two
print(boolean)

# ----------------------------------------
# 并集方法
'''
集合的并：
set1.union(set2, set3…)
返回值：返回一个新集合;
'''
_x = {2, 3, 11, 8, 9}
x4 = {12, 3, 7, 8, 8, 9, 15}
x5 = {12, 15, 21, 11, 12, 17}
var = _x.union(x4)  # variable变量
print("结果是:", var)  # 输出结果是有序的！
# print(_x.union(x4))

# ----------------------------------------
# 交集方法
'''
集合的交：
set1.intersection(set2, set3,…)
    返回值：返回一个新集合
set1.intersection_update(set2,set3)
    用于获取两个或更多集合中都重叠的元素，即计算交集。
    返回值：没有返回值，在原始的集合上移除不重叠的元素
'''
print('有没有结果呢？', x4.intersection(_x))

# unresolved reference（参考） 未引用参考值
x4.intersection_update(_x)  # 可知为 8,9,3 ，看输出结果对不对
print(x4)

# ----------------------------------------
# 差集方法集合的差：
'''
set1.difference(set2, set3,…)
    返回值：返回一个新集合
set1.difference_update(set2,set3)
    返回值：没有返回值，在原始的集合上移除不重叠的元素
'''

# update 使用并集并更新集合内容 --- 可以将一个元素加到调用此方法的集合内 [集合A.update(集合B)]
# 可以 copy 浅复制

# print(x5.difference(_x))
# print(x5.difference_update(_x))  # update 更新;  输出结果为“none”空
x5.difference_update(_x)
print(x5)

# ----------------------------------------
# 判断集合关系
'''
set1.isdisjoint(set2)
    判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
set1.issubset(set2)
    判断set1是否是set2的子集，是则返回true,否则返回false
'''
set1 = {1, 3, 4, 7}
set2 = {2, 3, 5, 9}
print(set1.isdisjoint(set2))  # disjoint sets 不相交集
print(set1.issubset(set2))  # subset子集

# --------------------------------------------------------------------
# 冻结集合 frozenset
#   set是可变集合，frozenset是不可变集合也可直译为冻结集合，这是一个新类型的class。
#   设定后的冻结集合不可更改。
# 冻结集合建立完成后，不可使用基本函数，但可以使用集合函数（例如：isdisjoint、copy等）
m = frozenset([1, 3, 5])
n = frozenset([5, 7, 9])
print(m, n)
print("交集=", m & n)

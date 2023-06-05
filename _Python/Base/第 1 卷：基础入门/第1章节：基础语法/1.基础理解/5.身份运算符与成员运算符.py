# 身份运算符：
#       用于比较两个对象是否对应同样的存储单位
# is：           x is y
#       如果x和y对应同样的存储单位，则返回True；否则，返回False
# is not :      x is not y
#       如果x和y不对应同样的存储单位，则返回True；否则，返回False

x, y = 15, 15
print(id(x))
print(id(y))  # 利用id函数可以查看一个数据的内存首地址。
print(x is y, end=';')
print(x is not y, end=';')

x, y = [1, 2, 3], [1, 2, 3]
print(x is y, end=';')
print(x is [1, 2, 3], end=';')
print(x is y, end='||||')

"""
注释： 程序在运行时，输入数据和输出数据都是存放在内存中。
      内存中的一个存储单元可以存储一个字节的数据，每个存储单元都有一个唯一的编号，称为内存地址。

      根据数据类型不同，其所占用的内存大小也不同。
      一个数据通常会占据内存中连续多个存储单元，起始存储单元的地址称为该数据的内存首地址。
"""

#       x is y  等价于  id(x)==id(y)，
#       即判断x和y的内存首地址是否相同;

#       x is not y  等价于  id(x)!=id(y)，
#       即判断x和y的内存首地址是否不相同。


# -----------------------------------------------------------------------------

# 成员运算符：
#       用于判断一个可迭代对象(序列、集合或字典)中是否包含某个元素。
# in:       x in y
#       如果x是可迭代对象y的一个元素，则返回 True;否则，返回 False;
# not in:      x not in y
#       如果x不是可迭代对象y的一个元素，则返回 True;否则，返回 False;

x, y = 15, ['abc', 15, True]
print(x in y, end=';')

x = 20
print(x not in y, end=';')

y = (20, 'python 学习')
print(x in y, end=';')

x, y = 'py', 'python 学习'
print(x in y, end=';')

x, y = 'one', {'one': 1, 'two': 2, 'three': 312}
print(x in y, end=';')

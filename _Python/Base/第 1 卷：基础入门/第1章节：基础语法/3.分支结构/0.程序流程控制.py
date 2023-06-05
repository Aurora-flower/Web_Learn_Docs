# 为何需要程序流程控制？
"""
一个程序如果按部就班从头到尾，中间没有转折，其实是无法完成太多工作的，
设计过程难免会需要转折，这个转折在程序设计的术语称为流程控制。

涉及到关系运算符与逻辑运算符.
"""

# 顺序结构，循环结构，选择结构
# --------------------------------------------------
# 列表生成 list generator 的应用
# 新列表 = [表达式  for 项目 in 可迭代对象]
n = int(input("请输入一个整数："))
if n > 10:
    n = 10
square = [num ** 2 for num in range(1, n + 1)]
print(square)

# --------------------------------------------------
# 打印含列表元素的列表
colors = ['Red', 'Green', 'Blue']
shapes = ['circle', 'square']
result = [[colors, shapes] for color in colors for shape in shapes]
'''
for shape in shapes:
    for color in colors:
        result = [colors,shapes]
'''
for color, shape in result:
    print(color, shape)

# --------------------------------------------------
# 生成含有条件的列表
# 新列表 =[表达式 for 项目 in 可迭代对象 if 条件式]

# 传统方法
oddlist = []
# for number in range(1, 10):
#     if number % 2 == 1:
#         oddlist.append(number)

# print(oddlist)

# python精神
oddlist = [number for number in range(1, 10) if number % 2 == 1]
print(oddlist)


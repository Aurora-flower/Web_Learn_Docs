# ctrl + . 为 英文/中文 标点符号切换
# pycharm的撤回快捷键为 ctrl+shift+z
# pycharm有自动调整代码格式的快捷键，默认为 Alt+Ctrl+L

"""
在其他程序语言中，相类似的功能是称为数组(array)。
不过，python的列表功能除了可以存储相同的数据类型，也可以存储不同的数据类型。
比如，列表中可以同时含有整数、浮点数、字符串，或是其他的列表或是字典(dict)
"""

# 列表的基本定义：
#   格式： name_list = [element1,element22,element3...]
#   基本上列表内每一个数据都称为元素，元素放在[]内，彼此用逗号","分隔。可以存储不同的数据类型。

# ----------------------------------------
# 第一节：列表list{定义，访问，添加，删除}，用中括号
# 访问：通过 index索引，读取列表元素
'''
列表中每个元素之间用逗号分隔，
正索引从0开始，负索引从-1开始
'''
a = [555, 666, 777, 888]
b = []  # 从输出的结果来看，python语言中，列表内是否有空格是不影响的

# 当列表内全是数值型数据时，可以用 max()、min()函数、sum()
#     max()函数可以获得列表的最大值
#     min()函数可以获得列表的最小值
#     sum()函数可以获得列表的总和

print("最大值：", max(a))
print("最小值：", min(a))
print("总和：", sum(a))

# ----------------------------------------
# 列表的元素截取(列表切片 list slices)
#   截取规则：左闭右开 ，[开始：结束：步长] ；
#   发现： 输出截取索引时，str好像可以省略
print(">>>截取：", str(a[1:3]))
# print(">>>原来的a[1:3]的值：", a[1:3])


# 列表的重新赋值
a[1] = [999]
a[2] = 100
print(">>>替换了a[1:3]的值：", a[1:3])

# index 方法可以用于从列表中找出某个值第一个匹配项的索引位置
# 即返回特定元素内容第一次出现的索引值
order_list = [1, 2, 3, 4, 5, 6]
print("索引位置", order_list.index(4))

# ----------------------------------------
# 列表的元素添加
#   [append方法用于末尾添加],append方法也可以将某一列表添加到另一列表的末尾 [列表A.append(列表B)]。
number_list = [1, 5, 8, 2, 4, 1, 8]
print("添加前 =", number_list[-1])
# append的意思是“追加；（在文章后面）附加，增补”，顾名思义是默认结尾添加
number_list.append(666)

# insert方法用于将对象插入到列表中，指定索引
number_list.insert(3, 'char')
print("添加后 =", number_list[3])

# 区别:
#     append()方法固定在列表末端插入元素，insert()方法则是可以在任意位置插入元素

# ----------------------------------------
# 列表的相加：
#       [“+”]，允许进行列表间的相加，即结合
#   [列表元素的组合join:]
#       char.join(seq)  # seq表示参数必须是列表、元组等序列数据
#       char 则是组合后各元素之间的分隔字符，可以是单一字符，也可以是字符串
char = ''
Char_List = ['你好!', '世界!', '再见!']
JOIN = char.join(Char_List)
# ''.join(iterate)
print("联合：", JOIN)

# extend(扩展)方法:
#   可以在列表的末尾一次性追加另一个序列中的多个值
#   与"+"的区别是，原始的连接操作是会返回一个全新的列表，extend则是修改原来的变量值
x = [1, 2, 3]
y = [4, 5, 6]
data = x.extend(y)
print(data)
# print(type(x.extend(y)))  # None

# ----------------------------------------
# 列表的元素删除 del \ remove \ pop(pop有一个返回值)

# delete 删除
#   del()方法缺点：资料删除就无法获取相关信息
data_list = [1, 5, 8, 2, 4, 1, 8]
del data_list[-2]
print("del删除索引-2的元素：", data_list)  # number_list = [1, 5, 8, 2, 4, 8]

# remove()方法:
#   删除指定（内容）元素，若要用此方法删除所有相同的元素，必须使用循环。
data_list.remove(8)  # 若是列表内有相同的元素，则只删除第一个出现的元素。
print("remove删除指定一个元素：", data_list)

# pop()方法：
#   删除后将弹出所删除的值；若未指明所删除元素的位置，一律删除末尾的元素
data_list.pop()  # 默认删除列表最后一个内容
print(data_list.pop())
print("pop随机一个元素：", data_list)

# ----------------------------------------
# count方法统计某个元素在列表出现的次数
# times = list_name.count(搜寻值)
lis = [1, 1, 1, 1, 1, 3, 7, 9]
print("1出现的次数:", lis.count(1))

# ----------------------------------------
# 颠倒排序 reverse()
# reverse 方法将列表中的元素反向存放
lis.reverse()
print(lis)

# ----------------------------------------
# 排序 sort()
# sort 方法用于在原位置对列表进行正排序
# 可以在 sort()增加参数"reverse = True"由大到小的倒排序。此方法，将造成列表的元素顺序永久更改
sort_list = [1, 5, 7, 0, 2, 7, 8, 4, 9]
print(sort_list.sort())  # None   object.sort(reverse=True)

# 排序 sorted()
# 此方法，可以获得想要的排序效果，可以用新的列表存储新的排序列表，也不会对原先的列表更改
equal = sorted(sort_list)
print(equal)

# ----------------------------------------
# len()函数获得列表的元素个数

# 列表的复制
# 列表乘以一个n数字，即重复n次

# ----------------------------------------
# 列表的深复制(deep copy)
#   只要以一个列表更改元素会影响到另一个列表同步更改的复制称为深复制(deep copy)
"""
print('===========变化前============')
# 选择的运动
mySports = ['basketball','baseball']
friendSports = mySports

# 选择的运动项目的地址
print('mySport address =',id(mySports))
print('friendSport address =',id(friendSports))

# 喜欢的运动
print('I like sports =',mySports)
print('my friend like sports =',friendSports)

# 添加运动项目
mySports.append('football')
friendSports.append('soccer')


print('============变化后============')
# 选择的运动
print('mySport new address =',id(mySports))
print('friendSport new address =',id(friendSports))

# 喜欢的运动
print('I like new sports =',mySports)
print('my friend like new sports =',friendSports)
"""

# ----------------------------------------
# 列表的浅复制(shallow copy)
# id()函数可以获得变量的地址
#   执行复制后，当一个列表改变后，不会影响到另一个列表的内容
print('===========变化前============')
# 选择的运动
mySports = ['basketball', 'baseball']
friendSports = mySports[:]  # 注意此处

# 选择的运动项目的地址
print('mySport address =', id(mySports))
print('friendSport address =', id(friendSports))

# 喜欢的运动
print('I like sports =', mySports)
print('my friend like sports =', friendSports)

# 添加运动项目
mySports.append('football')
friendSports.append('soccer')

print('============变化后============')
# 选择的运动
print('mySport new address =', id(mySports))
print('friendSport new address =', id(friendSports))

# 选择的运动项目的地址
print('I like new sports =', mySports)
print('my friend like new sports =', friendSports)

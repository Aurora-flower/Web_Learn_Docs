# 列表 list 与元组 tuple是依序列排列的可称为序列数据结构，只要知道元素的特定位置，即可使用索引观念取得元素内容。
# 字典：
#   并不是依序列排列的数据结构，通常可称为非序列数据结构。
#   可以内含不同数据类型的元素。

# -----------------------------------------------------------
# 字典dictionary {定义，引用，增加，删除}，用中括号，且无序
Z = {
    '距离考试': 35,  # 格式“key：value”键值对，构造元素
    '想攒多少钱': 10000,
    '升本需要多少分': 550,
}
print(Z)
# 访问
print(Z['距离考试'])  # 引用 key

# ------------------------------
# 修改
Z['距离考试'] = 34  # 改变 key值,进行赋值。格式： 字典[key] = x
print(Z)

# ------------------------------
# 增加
Z['彩礼多少钱'] = 3000000  # 当赋值的 key不存在时，则为字典增加
print(Z)

# ------------------------------
# 删除特定字典元素
del (Z['升本需要多少分'])
print(Z)

# -----------------------------------------------------------
# 字典遍历
dictionary = {
    'title': 3,
    'info': 7,
    'thesis': 4
}

for key, value in dictionary.items():
    print(key, value)

"""
遍历字典：
items(): 返回字典内的 key-value 键值对
keys(): 返回字典内所有 key 列表
values(): 返回字典内所有 value 列表 
"""
# 遍历字典
# 字典(Dictionary).items() 函数以列表返回可遍历的(键, 值) 元组数组。
for left, right in dictionary.items():
    print('遍历字典:', left, right)

# 遍历字典 key值
for var in dictionary.keys():  # 这里的keys可以看做是函数，而不是对象；
    print('遍历字典 key值:', var)

# 遍历字典 value值
for var in dictionary.values():
    print('遍历字典 value值:', var)

# 排序与遍历字典
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内置函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
for variable in sorted(dictionary.values()):
    print('排序与遍历字典:', variable)
    # print("区别：",variable,dictionary[variable])

# -----------------------------------------------------------
# 字典的复制
fruits = {'banana': 2, 'apple': 7, 'pear': 'none', 'orange': 9}
c_fruits = fruits.copy()  # 所复制的儿字典是独立存在新地址变量中
print(c_fruits)

# 验证字典元素是否存在
#   键 in name_dict
key = input("请输入键（key）：")
value = input("请输入值（value）：")
if key in c_fruits:
    print("%s已经在字典了" % key)
else:
    c_fruits[key] = value
    print("新的字典内容:", c_fruits)
# -----------------------------------------------------------
# 建立字典 dict()内置函数
def_dict = dict(国泰君安证券=5016,小荷花=1327,银行卡=350)
print(def_dict)

# 建立字典 fromkeys()
#   name_dict = dict.fromkeys(seq,value)
#   使用sqe（sequence）序列建立字典。若是未设定 value，则用 None当字典的键的值。
sequence = ['name', 'nation', 'city']
seq_dict = dict.fromkeys(sequence)
print("创建字典：", seq_dict)

# -----------------------------------------------------------
# 搜寻字典
#   get()、setdefault()函数

# get()
#   搜寻字典的键，如果存在则返回该键的值，如果不存在则返回默认值
#   return_value = dict.get(key,default=none)
#       dict是想要搜寻的字典，key是要搜寻的键。如果找不到 key则返回 default（未设则返回 None）。
ret_value = fruits.get('orange')
print(ret_value)

# setdefault()
#   该方法与 get()基本相同，不同之处在于 get()方法不会改变字典内容。
#   ret_dict = fruits.setdefault('data',default=none)
#   使用 setdefault()方法时若搜寻的键不在，会将 [键-值] 加入字典。
#   如果有设定默认值则将 [键-默认值]加入字典；如果未设定默认值则将 [键-None]加入字典；

ret_dict = fruits.setdefault('data',12)
print("return:", ret_dict)
print(fruits)

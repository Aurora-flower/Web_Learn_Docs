# dir()函数
#   可以列出所有的内置函数
BIF = dir(__builtins__)
for i in BIF:
    print(">>>", i, end=';\n')

# help()函数查看 function功能

"""
{数据类型}:

Integer 整数          -256, 16
String 字符串       "hello", '你好'
Boolean 布尔值      True, False
List 列表         [ value, ... ]
Tuple 元组          ( value, ... )
Dictionary 字典      { key: value, ... }
Set 集合          {value,value, ... }
"""

# -----------------------------------------------

"""
{内置函数}:

[交互操作]:
print()     向标准输出对象打印输出
input()     读取用户输入值
[数学运算]:
abs()       返回数字的绝对值
div-mod()    返回两个数值的商和余数
max()       求最大值
min()       求最小值
pow()       返回两个数值的幂运算值
round()     元素求和，五舍六入
sum()       四舍五入求值

[类型转换]:
bool()      返回一个布尔值
dict()      创建一个字典
int()       将一个字符串或数字转换为整型
float()     返回或转换浮点数
tuple()     创建元组
set()       创建一个新的集合
str()       将对象转化为字符串
list()      创建一个字典
complex()       返回或转换复数
bytearray()     返回字节数组
bytes()     创建一个不可变字节数组
memory-view()        创建内存查看对象
ord()       返回Unicode字符对应的整数
chr()       返回整数所对应的Unicode字符
bin()       将整数转换成2进制字符串
oct()       将整数转化成8进制数字符串
hex()       将整数转换成16进制字符串
frozenset()     创建一个新的不可变集合
enumerate()     根据可迭代对象创建枚举对象
range()     创建一个新的range对象
iter()      创建一个新的可迭代对象
slice()     创建一个新的切片对象
super()     创建一个新的子类和父类关系的代理对象
object()     创建一个新的object对象

[序列操作]:
all()       判断每个元素是否都为True值
any()       判断可迭代对象的元素是否有为True值
filter()        过滤可迭代对象的元素
map()       映射生成新的可迭代对象
next()      返回可迭代对象中的下一个元素值
reversed()      反转序列生成新的可迭代对象
sorted()        排序，返回一个新的列表
zip()       聚合传入的每个迭代器中相同位置的元素，返回一个新的元组类型迭代器

[对象操作]:
help()      返回对象的帮助信息
dir()       返回对象属性列表
id()        返回对象的唯一标识符
hash()      获取对象的哈希值
next()      返回可迭代对象中的下一个元素值
type()      返回对象的类型
len()       返回对象的长度
ascii()     返回对象的可打印表字符串表现方式
format()        格式化显示值
vars()      返回对象的属性列表

[反射操作]:
__import__()        动态导入模块
isinstance()        判断对象是否是类的实例
is-subclass()       判断对象是否是子类
hasattr()       检查对象是否含有属性
getattr()       获取对象的属性值
setattr()       设置对象的属性值
delattr()       删除对象的属性
callable()      检测对象是否可被调用

[变量操作]:
globals()       返回当前作用域内的全局变量
locals()        返回当前作用域内的局部变量

[文件操作]:
open()      使用指定的模式和编码打开文件，返回文件读写对象

[编译执行]:
eval()      执行动态表达式求值
exec()      执行动态语句块
repr()      返回一个对象的字符串表现形式
compile()       将字符串编译为代码或者AST对象，使之能够通过exec语句来执行或者eval进行求值

[装饰器]:
property()      标示属性的装饰器
class-method()       标示方法为类方法的装饰器
staticmethod()      标示方法为静态方法的装饰器
"""

# -------------------------------------------------

"""
{字符串 String}:


[查找与替换]:
count(sub)      统计字符串里某个字符sub出现的次数。
find(sub)       检测返回sub索引位置，否则返回-1
index(sub)      检测返回sub索引位置，否则抛出异常
rfind(sub)      从右侧开始查找返回sub索引位置
rindex(sub)     从右侧开始返回sub索引位置
replace(old,new)        用new替换old
注意：前面五个方法都可以接受start开始、end结束位置参数，

[性质判定]:
isalnum()       是否全是字母和数字
isalpha()       是否全是字母
isdigit()       是否全是数字
islower()       是否全是小写
isupper()       是否全是大写
isspace()       是否全是空白字符
istitle()       第一个字符是否为大写
startswith(prefix)      是否以指定字符开头
endswith(suffix)        是否以指定字符结尾

[分割与连接]:
partition(sep)      用指定字符串分割为元组
rpartition(sep)     从右边开始分割
splitlines()        用换行符分割为列表
split(sep)         用指定字符串分割为列表
rsplit(sep)     从右边开始分割

[大小写转换]:
lower()     字符串转小写
upper()     字符串转小写
capitalize()        首字母大写
swap-case()      交换大小写
title       每个单词首字母大写

[删减与填充]:
strip([chars])      移除头尾指定字符串(默认空白)
strip([chars])      移除右边指定字符串(默认空白)
zfill(width)        原字符串居右，返回指定宽度字符串，前面用0填充
center(width[,fchar])       原字符串居中，返回指定宽度字符串，用fchar填充
ljust(width[,fchar])        原字符串居左，返回指定宽度字符串，用fchar填充
rjust(width[,fchar])        原字符串居右，返回指定宽度字符串，用fchar填充
expandtabs([tabsize])       把tab转换为空格，默认是8个
"""

# ------------------------------------------------
"""
{语句}:

[if语句]
if 表达式:
    语句1
elif 表达式:
    语句2
else:
    其他语句

[while循环]
while 表达式:
    语句

[for循环]
for var in 集合列表:
    语句

[for与range循环]
for i in range(开始值, 结束值 ,[间隔]):
    语句
 # 结束值是不包含的，开始值包含

[函数定义]
    def name(arg1,arg2,...)
        statement
        return 返回值
"""

#  -----------------------------------------------------------------

"""
{算术运算符}:
x + y       加
x - y       减
x * y       乘
x / y       除
x % y       取模,返回除法的余数
x ** y      幂，返回x的y次幂

x // y      取整除
"""

# -------------------------------------------------------
"""
{比较运算符}:
x < y       小于
x <= y      小于等于
x > y       大于
x >= y      大于等于
x == y      相等
x != y      不等
"""

# -------------------------------------------------------
"""
{布尔运算符}:
not x       非
x and y     且
x or y      或
"""

# -------------------------------------------------------
"""
{转换函数}:
int(expr)       将expr转成整型
float(expr)     将expr转成浮点型
str(expr)       将expr转成字符串
chr(num)        将num转成ASCII字符
"""

# ------------------------------------------------------

"""
{String字符串 / List列表 / Tuple操作}:
len(s)      s长度
s[i]        取s中的第i个值 (从0开始)
s[start :end]      从开始（包括）到结束（不包括）的片段
x in s      如果x包含在s中则为true
x not in s       如果x不包含在s中，则为true
s + t       把s与t的相连接
s * n       将s复制n份
sorted(s)       对s进行排序
s.index(item)       item在s中的位置
"""

# ----------------------------------------------------------
"""
{列表 List}:

[删除]
del(item)       删除指定的列表
pop([item])     删除并返回指定元素，默认为最后一个
remove(item)        移除指定元素

[列表操作]
len(ls)     计算列表的长度
max(ls)     返回列表最大值
min(ls)     返回列表最小值
list(seq)       元组转换为列表

[列表排序]
sort()      永久排序
sorted(ls)      临时排序
reverse()       翻转列表

# -------------------------------------------------
[列表切片]
正序索引从0开始，逆序索引从-1开始；

[start:end]     从start 提取到end - 1；
[start:end:step]        从start 提取到end - 1，每step 个字符提取一个；
[:]         提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串；
[start:]        从start 提取到结尾；
[:end]      从开头提取到end - 1；


list = [1, 2, 3, 4, 5, 6, 7]

list[2:5]       # [3, 4, 5]

list[0:7:2]     # [1,3,5,7]

list[0:]    #列出索引0以后的[1, 2, 3, 4, 5, 6, 7]

list[1:]    #列出索引1以后的[2, 3, 4, 5, 6, 7]

list[:-1]   #列出索引-1之前的[1, 2, 3, 4, 5, 6]

list[1:3]   #列出索引1到3之间的-----[2]

list[::-1]  #[7, 6, 5, 4, 3, 2, 1]

# ----------------------------------------------------
{range函数}:

range() 函数可创建一个整数列表，一般用在 for 循环中
格式：    range(start, stop[, step])

start: 计数从 start 开始。默认是从 0 开始。
stop: 计数到 stop 结束，但不包括 stop。
step：步长，默认为1

range(7)    # 从 0 开始到 7
            # [0, 1, 2, 3, 4, 5, 6, 7]

range(1, 7)     # 从 1 开始到 7
                # [1, 2, 3, 4, 5, 6]

range(0, 30, 5)     # 步长为 5
                    # [0, 5, 10, 15, 20, 25]
"""

# --------------------------------------------

"""
{字典 Dictionary}:

pop(key)        删除指定的键
clear()     清除所有的键与值
dic['age']=13   增或该age值为13
get(key)        查找指定键的值没有返回None
setdefault(key)     查找指定的键，没有返回None
update(dic2)        合并更新字典
keys()      返回所有键列表
values():       返回所有值列表
items():        返回可遍历的(键,值)元组列表
"""

# --------------------------------------

"""
{set 集合}:

add(item)       增加一个值
update(items)       更新多个值
remove(item)        移除指定值
"""

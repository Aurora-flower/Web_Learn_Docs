# 字符串数据类型：
#   所谓字符串（string）是指两个单引号或双引号之间任何个数字符的数据，数据类型代号”str“。
# 若引号内有空格，也会在输出变量时一起输出
print(str(124))  # str()函数可以强制将数值数据转换为字符串数据

# -------------------------------------------
# 字符串数据的转换
"""
Python 有办法将任意值转为字符串：
     将它传入repr () 或str ()函数。
     函数str () 用于将值转化为适于人阅读的形式，而repr () 转化为供解释器读取的形式.

官网解释：
     repr（）函数得到的字符串通常可以用来重新获得该对象，repr（）的输入对python比较友好.
"""
# help(ord)
# ord(x) ----可以返回单字符字符串的 Unicode 码位。
# 中文字也可以传回Unicode码值。英文字符的Unicode码与ASCII码值一样
ord('s')
# chr(x) ----可以返回函数x的字符，x是ASCII码值。
chr(12)

# -------------------------------------------------------------
# 格式输入输出
# reference参考（值）要存在

# 我们已经知道输出print，那输入input会用吗？
str1 = "python 学习"
str2 = '我喜欢'
print(str1, "学习", str2)

# format()函数,译为格式，增强版的格式化输出功能 ’f{}‘
print("{}学习{}".format(str1, str2))
print(f"{str1}学习{str2}")  # 另一种用法

"""
格式化输出:(占位符号)
  %d 格式化整数输出
  %f 格式化浮点数输出
  %o 格式化8进位数输出
  %x 格式化16进位数输出
  %s 格式化字符串输出
"""
print("%s学习%s" % (str1, str2))  # 此处，%前不能有逗号，C语言中有逗号

# -------------------------------------------------------------
"""
精准格式化的输出:
  %(+|-)nd 格式化整数输出
  %(+|-)m.nf 格式化浮点数输出;  在浮点数中,m 代表保留多少格数供输出(包含小数点), n 则是小数点保留格数.
  %(+|-)no 格式化8进位数输出
  %(+|-)nx 格式化16进位数输出
  %(+|-)ns 格式化字符串输出
"""
# 除了浮点数,其他的n则是保留多少格数空间.
# 负号(-):表示保留个数多时,数据将靠左输出;
# 正号(+):表示输出数据是正值时,将在左边加上正值符号
x = 5
print("x=%+6d" % x)  # 若是保留格数空间太多则数据右对齐.
print("x=%-6d" % x)  # 若是保留格数空间不足,则是完整输出数据;

# -------------------------------------------------------------
# input不支持并行输入
user = input("用户名：")
# print("用户名：", user)

passage = input("密码：")
# print("密码：", passage)

# ------------------------------------------
# 字符串与整数相乘产生复制效果
print(" " * 40)  # 空格也会被打印

number = input("请输入一个数值：")  # 默认输入字的是符串数据类型
print(number * 2)  # 这里的x是字符串，输出结果重复两次
print(int(number) * 3)  # 先将字符型转为数值型，才可以得到数值乘法运算结果

# ------------------------------------------
# 转义字符的取消

# 在字符串前加上r，可以防止逸出字符被转译；
print(r"我\n喜欢\n你")
# r功能：取消转义字符的功能

# -------------------------------------------------------------
# len():   函数返回对象中项目的数量。当对象是字符串时，len() 函数返回字符串中的字符数
# lower(): 将字符串转成小写字
# upper(): 将字符串转成大写字
# title(): 将字符串转成第一个字母大写，其他是小写
# strip(): 删除字符串头尾两边多余的空白
# rstrip(): 删除字符串尾端多余的空白
# lstrip(): 删除字符串开始端多余的空白

# -------------------------------------------------------------
# dir()获得系统内部对象的方法
# list_function = dir(list)
# print(list_function)

# -------------------------------------------------------------
# 字符串切片
# 参考列表的读取方法：
#   除了会更改内容的列表函数或方法不可应用在字符串，其他的都可以
'''
截取：
0位置时不能为空；
左闭右开 [开始：结束），不包含结束位置；
索引排序从0开始,步长默认为1；
'''
# 基本格式为：    string-name[start：stop：step]
string = "parameter参数"
print(string[3:6:2])

# 可以用list将字符串转为列表
print(list(string))

# len():   函数返回对象中项目的数量。当对象是字符串时，len() 函数返回字符串中的字符数
print(len(string))
# -------------------------------------------------------------
# 也可以用 max()、min()函数，获得字符串中的最大或最小的字符（ASCII码）

# 将字符串处理为列表
x = list("Deep Stone")
print(x)

# split()方法：
#   可以将字符串以空格为分隔符，将字符串拆开,变成一个列表。一般适用于纯英文文件。
y = "Hello World !"
t = "你好 世界"
s_list = t.split()
print(s_list)

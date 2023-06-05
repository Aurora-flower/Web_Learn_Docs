from datetime import datetime

# --------------------------------------
# 函数read()
# msg = f.read(size)
#       逐个字节或字符读取文件中的内容，有参数时，读取参数size大小的字节


# 调用read（）一次将文件内容读到内存，但是如果文件过大，将会出现内存不足的问题。
# 一般对于大文件，可以反复调用read（size）方法，一次最多读取size个字节。

# """
# with open("lesson.txt", 'r') as f:    # 当前文件夹路径下,可以直接输入文件名
#     x = f.read(4)                     # 输入4,表示读取前4个字符
#     print(x)
# """

# --------------------------------------
# 函数readline()
#       var = f.readline()
# 可以每次读取一行内容，逐行读取文件的内容


with open("lesson.txt", 'r') as f:  # 当前文件夹路径下,可以直接输入文件名
    line = f.readline()
    # print(line)         # 读到一行,包含结果的换行。print又换行,多出一个换行
    # print("===============")

# 把末尾的换行"\n"删掉:
    # print(line, end='')  # 默认end值是换行符 \n
    # print("===============")

    # print(line.strip())   # strip剥夺
    # print("===============")
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符

    # line1 = f.readline(8)   # 读取参数指定个数的字符
    # print(line1, end=';')


# --------------------------------------
# 函数readlines()
#       var = f.readlines()
# 调用readlines（）一次读取文件中的所有内容并按行返回列表。

#
# with open("lesson.txt", 'r') as f:
    var = f.readlines()
    for i in var:
        print(i, end='')
#

# --------------------------------------

# # 格式控制
# #   引入datetime模块
# with open("lesson.txt", 'r') as f:
#     for line in f.readlines():
#         myDate, price = line.split(",")  # split 分离
#         gf = datetime.strptime(myDate, '%Y/%M/%d')
#         # print(gf)
#         # 序列多态性 ,%Y/%M/%d 年/月/日
#         price = float(price)
#         print("时间:", str(gf.date()) + ",销售额:" + str(price))
# # error:    时间错误

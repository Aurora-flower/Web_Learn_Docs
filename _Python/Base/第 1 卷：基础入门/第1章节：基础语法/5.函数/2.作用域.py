# 作用域：

"""
Python变量的作用域一共有4种，分别是：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域 以 L –> E –> G –>B 的规则查找，
即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
"""


# 声明全局变量
def law():
    global rule  # global，声明全局变量，在函数体内改变全局变量的值；
    # global 全球的；全世界的；整体的；全面的；总括的
    rule = "无法无天"
    print(rule)  # 在函数体内改变全局变量的名称，不影响全局值；


# ------------------------------------------------------------------------
# 所谓的函数（function）其实就是一系列的指令语句组成。

# 无参数返回值函数
def talk():
    message = "我喜欢学习python编程"  # message 消息，信息
    print(message)  # 函数体内有定义


# print(message)  此代码报错，涉及到局部变量问题；
# 在函数体内定义的message，，它的作用范围仅限于函数体内；
# 离开函数体，其中的变量就消失了；
# 个人理解：定义的是talk，而不是message；message字符串语句只是用来理解自己自定义的函数；

# ------------------------------------------------------------------------
# 参数传递
#   可以是一个或多个参数,数据类型可以为: 数值型,字符(串)型,字典,列表...
def box_volume(length, width, height):
    """L（length）、W（width）、H（height）"""
    volume = length * width * height
    return volume
    # print(volume)


# 字符串参数时,可以使用 middlenname =''默认为空字符串处理

# 关键词参数 （参数名称=值）
'''
所谓关键词参数（keyword arguments）是指调用函数时，参数时用 [参数名称=值]配对方式呈现。
'''
constant = box_volume(length=1, width=2, height=3)
print(constant)

# 参数值的默认处理
value = box_volume(1, 2, 3)
print(value)


# 函数返回值
# （函数没有 return，则自动处理为 return None）
def greeting(name):
    print('hi', name)


# ret_value = greeting('蓝花楹')
# print("返回值：", ret_value)      # 返回值为 None

# ------------------------------------------------------------------------



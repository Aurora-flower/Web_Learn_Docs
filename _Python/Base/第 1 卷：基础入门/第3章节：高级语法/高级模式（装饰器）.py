# 定义四个函数，分别完成加减乘除
# 在每次输出计算结果之前,先输出一个分隔线(=====)
# --------------------------------
# 方案一，单独定义一个show函数，用于输出分隔线
# 方案二，在定义的加减乘除函数中，增加print函数
"""
def myAdd(variable, element):
    # print("=====")
    return variable + element


def mySubtract(variable, element):
    # print("=====")
    return variable - element


def myMultiply(variable, element):
    # print("=====")
    return variable * element


def myDivide(variable, element):
    # print("=====")
    return variable / element


def show():
    print("=====开始=====")


show()
print(myAdd(2, 3))
show()
print(myDivide(2, 3))
show()
print(myMultiply(2, 3))
show()
print(mySubtract(2, 3))
"""

# --------------------------------
# 方案三，使用修饰器(假的)完成，
#       修饰器(假)，既可以有返回值，也可以没有返回值，样式多样
#       此时的缺陷：每次调用，都必须调用假修饰器的名称(show)
#       然后将实际函数作为参数
# 问题：无法直接使用实际函数的调用完成计算

"""
def Show(fun, variable, element):
    print("==========")
    var = fun(variable, element)
    print(var)


def MyAdd(variable, element):
    return variable + element


def MySubtract(variable, element):
    return variable - element


def MyMultiply(variable, element):
    return variable * element


def MyDivide(variable, element):
    return variable / element


Show(MyAdd, 3, 4)
Show(MySubtract, 3, 4)
Show(MyMultiply, 3, 4)
Show(MyDivide, 3, 4)

# 错误示范,直接引用
MyAdd = Show
MyAdd(3, 4)
"""
# --------------------------------
# 方案四：使用修饰器完成
# 修饰器，既可以有返回值，也可以没有返回值;样式多。
# 实现方式：实际函数值 = 修饰器函数名（实际函数名）

"""
def show(function):
    def temp(x, y):   # temp 临时
        print("==============")
        var = function(x, y)
        return var
    return temp


def myAdd(a, b):
    return a + b


def mySubtract(a, b):
    return a - b


def myMultiply(a, b):
    return a * b


def myDivide(a, b):
    return a / b


myAdd = show(myAdd)
print(myAdd(2, 4))
mySubtract = show(mySubtract)
print(mySubtract(4, 2))
myMultiply = show(myMultiply)
print(myMultiply(2,  3))
myDivide = show(myDivide)
print(myDivide(4, 2))
"""
# --------------------------------
# 方案五：使用修饰器语法糖： @修饰器
# 实现方式： @修饰器函数名
# 等价于：实际函数名=修饰函数名(实际函数名)
# 注意点：位置位于实际函数前

"""
def show(function):
    def temp(x, y):
        print("============")
        z = function(x, y)
        return z
    return temp


@show
def myAdd(a, b):
    return a + b


@show
def mySubtract(a, b):
    return a - b


@show
def myMultiply(a, b):
    return a * b


@show
def myDivide(a, b):
    return a / b


print(myAdd(2, 4))
print(mySubtract(4, 2))
print(myMultiply(2,  3))
print(myDivide(4, 2))
"""
# --------------------------------
# 上述过程中，参数的个数是固定的
# 优化：能够适应不同格式的参数

# args, arguments（参数）: 收集所有位置参数
# kwargs, keyword args: 关键字参数(字典等)

"""
def function(*args, **kwargs):
    print(args, kwargs)


function(6, "name", 名字=1234)   # 元组以” ，“分隔、结尾
"""
# --------------------------------
# 方案六：使用修饰器完成
# 可以使用不同格式的参数，2个或3个


def Decorator(function):    # 修饰
    # args 是 arguments 的缩写，表示位置参数；
    # kwargs 是 keyword arguments 的缩写，表示关键字参数。
    def cite(*args, **kwargs):    # cite 引用
        print("========开始分隔符=======")
        # *args就是就是传递一个可变参数列表给函数实参，这个参数列表的数目未知，甚至长度可以为0。
        # ** kwargs则是将一个可变的关键字参数的字典传给函数实参，同样参数列表长度可以为0或为其他值。
        var = function(*args, **kwargs)
        print(var)
        print("========结束分隔符=======")
        return var
    return cite


@Decorator
def myAdd(a, b):
    return a + b


@Decorator
def mySubtract(a, b):
    return a - b


@Decorator
def myMultiply(a, b):
    return a * b


@Decorator
def myDivide(a, b):
    return a / b


myAdd(2, 4)
print(myAdd(2, 4))
mySubtract(4, 2)
myMultiply(2,  3)
myDivide(4, 2)

# --------------------------------
# 综合练习案例：
# 设计一个修饰器，能够计算圆面积，正方形面积

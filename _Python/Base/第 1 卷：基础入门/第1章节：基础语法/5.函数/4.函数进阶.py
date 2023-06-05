# 局部函数
#   局部函数仅对同一文件中的其他函数可见。它们等效于其他编程语言的子例程，有时被称为子函数。

def computer(Type, t):
    def double(t1):
        return 2 * t1

    def half(t2):
        return t2 / 2

    def sqr(t3):
        return t3 * t3

    if type == "double":
        return double(t)
    elif type == "half":
        return half(t)
    else:
        return sqr(t)


print(computer("double", 10))
print(computer("half", 10))
print(computer("sqr", 10))

# --------------------------------------------------------------------
# 匿名函数 lambda：
#   是指一类无需定义标识符（函数名）的函数或子程序。
#   是一种小的匿名函数。可接受任意数量的参数(包括可选参数) ,并且返回单个表达式的值,但只能有一个表达式。
'''
    所谓的匿名函数(anonymous function)是指一个没有名称的函数，python是使用def定义一般函数，匿名
函数则是使用lambda来定义，有的人称为lambda表达式。
    
'''

# 语法：
#   lambda arguments : expression
# 其实 lambda返回值是一个函数的地址，也就是函数对象。
#   常与内置函数 filter()、map()等共同使用

"""
var = lambda x: x + 10
print(var(5))
"""


def calculation(mode):
    if mode == "addition":  # add , subtract , multiply and divide   加减乘除
        return lambda h: h + 2
    elif mode == "subtract":
        return lambda q: q - 5
    elif mode == "multiply":
        return lambda q: q * 3
    else:
        return lambda e: e // 2
    # 斜杠(/)运算的结果是浮点型；
    # 双斜杠(//)运算的结果是整型；


add_result = calculation("addition")
print(add_result(10))
sub_result = calculation("subtract")
print(sub_result(5))
mul_result = calculation("multiply")
print(mul_result(7))
div_result = calculation("divide")
print(div_result(7))


# -----------------------------------------
# 匿名函数使用 filter()
#   匿名函数一般是用在不需要函数名称的场合
#   内置函数：
#       filter(function,iterable)   # filter 滤波器,过滤 (含有判断)
#   作用： 依次对可迭代对象（可以重复执行）的元素放入 function（item）内，然后将 function()
#   函数执行结果是 True的元素(item)组成新的筛选对象(filter object)返回。

# 传统方法将列表中的奇数筛选出来(未使用 lambda)
def odd_fun(x):
    return x if (x % 2 == 1) else None


mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(odd_fun, mylist)
print("奇数列表:", [item for item in filter_object])

# 使用匿名函数重新设计
my_list = [5, 10, 15, 20, 25, 30]
odd_list = list(filter(lambda x: (x % 2 == 1), my_list))
print(f"奇数列表:{odd_list}")

# -----------------------------------------
# 匿名函数使用 map()
#   匿名函数一般是用在不需要函数名称的场合
#   内置函数：
#       map(function,iterable)    # (不含判断)
#   作用： 依次对可迭代对象（可以重复执行）的元素放入 function（item）内，然后将 function()
#   函数执行结果组成新的筛选对象(filter object)返回。

# 使用匿名函数
myList = [5, 10, 15, 20, 25, 30]
square_list = list(map(lambda x: x ** 2, mylist))
print(f"列表的平方值:{square_list}")


# --------------------------------------------------------------------
# 递归式函数设计 recursive
#       一个函数可以调用其他函数也可以调用自己,其中调用本身的动作称递归式(recursive)调用.
# 递归函数的特点:
#   每次调用自己时,都会使范围越来越小
#   必须要有一个终止的条件来结束递归函数
#   常见的应用：
#       处理正整数的阶乘 n!
#       阶乘观念是由法国数学家（医生）克里斯蒂安·克兰普(1760-1826)所发表

# 递归函数执行阶乘(factorial)
def factorial(n):
    # 计算 n的阶乘必须是正整数
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


value = 3
print(f"{value}的阶乘:", factorial(value))


# --------------------------------------------------------------------
# pass与函数
def fun(arg):
    pass  # 程序没有执行结果，待补充函数


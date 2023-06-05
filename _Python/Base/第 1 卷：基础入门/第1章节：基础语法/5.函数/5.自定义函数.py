# 自定义函数
"""
def 函数名(参数):
    函数体
    [return [返回值]]  # 参数 , return , 返回值 可选(可有可无)
"""


# -------------------------------------------------------
# 根据半径，计算圆的面积
def area1():  # area 面积
    print(3.14 * 10 * 10)  # 无参数、无返回值；


# 正方形(square)
def square(length, width):
    return length * width


print(square(3, 3))

# -------------------------------------------------------

"""
    ===========返回值总结===========
    如果没有返回值，直接调用函数，执行函数；
    如果有返回值，函数的运行结果，作为一个值来使用；

    ===========参数总结===========
    无参数，函数的功能是固定的。
    有参数，函数的功能使用更加灵活。
"""


# -------------------------------------------------------
# 基本传递处理任意数量的参数
def make_icecream(*toppings):
    # 列出制作冰激凌的配料
    print("配料如下:")
    for topping in toppings:
        print(f">>>{topping}")


make_icecream('草莓', '葡萄干', '巧克力')


# -------------------------------------------------------
# 含有一般参数与任意数量参数的函数(任意数量参数必须放在右边)
def make_icecream_type(icecream_type, *toppings):
    # 列出制作冰激凌的配料
    print(f"{icecream_type}配料如下:")
    for topping in toppings:
        print(f">>>{topping}")


make_icecream_type('纯牛奶', '香蕉', '奥利奥')


# -------------------------------------------------------
# 关键字参数
#   是指使用形式参数的名字来确定输入的参数值。
#   通过此方式指定函数实参时，不再需要与形参的位置完全一致，只要将参数名写正确即可。

# 含有一般参数与任意数量的关键字参数:    自定义建立字典函数
def built_dict(name, age, **players):
    # 建立 NBA球员的字典数据
    info = dict()
    info['name'] = name
    info['age'] = age
    # 遍历字典
    for key, value in players.items():
        info[key] = value
    return info  # 返回所建立的字典


player_dict = built_dict('James', '32',
                         city='Cleveland',
                         state='Ohio')  # state 声明,国家,州

print(player_dict)

# --------------------------------------------

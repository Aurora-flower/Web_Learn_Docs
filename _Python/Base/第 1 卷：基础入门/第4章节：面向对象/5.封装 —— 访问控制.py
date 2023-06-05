# 类的访问权限 —— 封装(encapsulation)

"""
封装：
      * 把数据(attribute)，实现(function)放在类内部完成，对外显示一个接口(能被调用的函数）
      * “封好的类，是一个黑盒子”
      * 与函数对比，类是更高层次的封装(更高级的函数)
      * 类，实现了更高层次的封装，不仅封装了操作，还封装了数据。
      * 使用set，get能够在设置之前，对数值逻辑进行判断
"""

# 类：实现，属性
# 函数：是实现

"""
公有（属性和方法）：
    从程序直接引用类内的属性，像这种类内的属性可以让外部引用的称[公有（public）属性],而可以
让外部引用的方法称为公有方法。
私有（属性和方法）：
    python也具有私有属性和方法的观念，主要精神是类外无法直接更改类内的私有属性，类外也无法直接调用私有方法，
这个观念又称为封装。
"""


# -----------------------------------------------------------------------------------------------
# 定义怪兽类
class Monster:
    def __init__(self, name, skill, health):  # 可以不初始化
        print("=======准备初始化")
        self.name = name
        self.skill = skill
        self.health = health
        print("========结束初始化")

    def show(self):
        print("hack")
        print("my name:", self.name)
        print("my skill:", self.skill)
        print("my health:", self.health)


hack = Monster("Slimes", "learn", 85)
hack.show()

# -----------------------------------------------------------------------------------------------
# 访问控制
"""
类型1(系统)：首尾都是下划线(类似“__xxx__”)变量，是特殊变量
类型2(保护)：可以被访问，但是，通常视为私有变量
类型3(私有)：双下划线开头，私有变量，无法直接使用
"""


class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # 私有，实现了隐藏，无论是age,__age都无法访问类内部数据，实现高级封装

    def show(self):
        print("my name:", self.__name)
        print("my age:", self.__age)

    def set_age(self, age):
        if age < 0:
            print("年龄不符合")
        else:
            self.__age = age

    def get_age(self):
        # print("my age:", self.__age)
        return self.__age


Yan = People("YanBin", 22)
Yan.show()
Yan.set_age(18)
print(Yan.get_age())
Yan.show()


# ---------------------------------------------------------
# 私有属性(private attribute)
#   为了确保类内的属性的安全，有必要限制外部无法直接获取类内的属性值.


# 如果有必要访问私有变量，采用方式：
#       [ Object.__ClassName__Private variables私有变量 ]
#   不建议访问访问类内部私有成员

# -----------------------------------------------------------------------------------------------
# 类的特殊属性

# __doc__ 属性 ：
#   文档字符串  __doc__ : 文档字符串的英文原意是文档字符串(docstring),函数或类的批注

def get_show(x, y):
    """文档字符串实例：
        建议 x,y是整数，这个函数将传回最大值"""
    if int(x) > int(y):
        return x
    else:
        return y


print(get_show.__doc__)


# -----------------------------------------------
# __name__属性
#   if __name__ == '__main__':
def main():
    print(get_show(2, 3))


if __name__ == '__main__':
    main()


# 总结： __name__可以判断这个程序是自己执行或是被其他程序import导入当成模块使用

# -----------------------------------------------------------------------------------------------
# 类的特殊方法

# -----------------------------------------------
# __str__()方法
#   协助返回易读取的字符串

# 未定义 __str__()方法的情况下，列出类的对象
class Name:
    def __init__(self, name):
        self.name = name


one = Name('HuaYing')
print(one)  # 结果不易读取

# 未定义 __str__()方法的情况下，列出类的对象
'''在 python 学习 shell 窗口输入two，获得的结果同样不容易阅读。'''


class Height:
    def __init__(self, height):
        self.height = height

    def __str__(self):
        return f"{self.height}"


two = Height("one hundred and seventy-nine centimeter(179 cm)")
print(two)
# -----------------------------------------------
# __repr__()方法
'''
    上述原因是，如果只是在Python Shell 窗口输入类变量 two，系统是调用__repr__()方法做响应。
    为了获得更容易阅读的结果，我们也需要定义此方法。
'''


class Weight:
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return f"{self.weight}"

    __repr__ = __str__


three = Weight("sixty-kilogram")
print(three)
# -----------------------------------------------
# __iter__()方法
'''
    建立类的时候也可以将类定义成为一个迭代对象，类似列表 (list) 、元组 (tuple),供for ...in循环
内使用,这时类须设计next()方法,取得下一个值,直到达到结束条件.
    为了防止迭代永远进行,可以使用 raise StopIteration.
'''


class Fib:
    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.maximum:
            # 为了防止迭代永远进行
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for i in Fib(100):
    print(i)

# -----------------------------------------------
# __eq__()方法
'''equal 相等. 判断2个字符串或其他内容是否相同'''


# equals()方法
class CityOne:
    def __init__(self, name):
        self.name = name

    def equals(self, city_one):
        return self.name.upper() == city_one.name.upper()


one = CityOne("HeNan")
two = CityOne("HuaYin 花楹")
three = CityOne("home")
print(one.equals(two))
print(one.equals(three))


# __eq()__取代equals()方法
class CityTwo:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        # def __eq__(self, city_two):
        return self.name.upper() == other.name.upper()
        # return self.name.upper() == city_two.name.upper()


one = CityTwo("HeNan")
two = CityTwo("HuaYin 花楹")
three = CityTwo("home")
print(one == two)
print(one == three)

# -----------------------------------------------------------------------------------------------
# 逻辑方法
#  *   __eq__(self,other)           *   self == other 等于
#  *   __ne__(self,other)           *   self != other 不等于
#  *   __lt__(self,other)           *   self  < other  小于
#  *   __gt__(self,other)           *   self  > other 大于
#  *   __le__(self,other)           *   self <= other 大于或等于
#  *   __ge__(self,other)           *   self >= other 小于或等于


# 数学方法
#  *   __add__(self,other)           *   self + other   加法
#  *   __sub__(self,other)           *   self - other   减法
#  *   __mul__(self,other)           *   self * other   乘法
#  *   __floordiv__(self,other)      *   self // other  整数除法
#  *   __truediv__(self,other)       *   self / other   除法
#  *   __mod__(self,other)           *   self % other   余数
#  *   __pow__(self,other)           *   self ** other  次方

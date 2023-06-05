# Object-oriented programming  面向对象编程(oop)
#        是一种程序设计思想，oop把对象作为程序的基本单元
#          一个对象包含了 数据（属性） 和 操作数据的函数（方法）
#               对象（object）和实例（instance）
#                   类属性没有值，对象属性有值
# ---------------------------------------------
# 特点：
#       可维护（修改方便）、
#       可复用（重复使用）、
#       可扩展（方便添加）、
#       灵活性好（横排竖排）

# ---------------------------------------------
# 三大特性：  封装、继承、多态

# ---------------------------------------------
"""
面向对象的基本概念:
1.对象
    对象是问题域中客观存在的事物的抽象，是一组属性和这些属性上操作的封装体。
    两个要素：
        属性用来描述对象的静态特征；
        操作用来描述对象的动态特征；
2.类
    具有相同属性和操作的一组相似对象（实体）的集合。
    组成：
        类的名字、类的属性、类的操作
3.消息
    消息是面向对象系统中，对象之间交互的途径，是向另外一个对象发出的服务请求，
    请求对象参与某一处理或回答某一要求的信息，是对象之间建立的一种通信机制。
4.封装
    指把对象的属性和操作给合成一个独立的系统单位，隐藏对象的内部细节。（信息隐蔽）
"""


# ---------------------------------------------
class Kind:
    print("类-----抽象化")


def object_():
    print("对象-----具象化")


Kind()
object_()


# ---------------------------------------------
# 几何数据的应用
class Geometric:
    def __init__(self):
        self.color = 'Green'


class Circle(Geometric):
    def __init__(self, radius):
        # 继承，但覆盖了init方法
        super().__init__()
        self.PI = 3.1415926
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_diameter(self):  # diameter 直径
        return self.radius * 2

    def get_perimeter(self):  # perimeter 周长
        return self.radius * 2 * self.PI

    def get_area(self):
        return self.PI * (self.radius ** 2)

    def get_color(self):
        return self.color


A = Circle(5)
print(f"圆的颜色:{A.color}")
print(f"圆的半径:{A.get_radius()}")
print(f"圆的直径:{A.get_diameter()}")
print(f"圆的周长:{A.get_perimeter()}")
print(f"圆的面积:{A.get_area()}")


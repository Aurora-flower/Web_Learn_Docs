"""
# 自上向下
    提供共享，以开发游戏为例：
        比如，游戏里面有很多种类不同的怪兽，不同的怪兽之间存在很多相同的属性、动作（方法）

    # 构造一个基类”怪兽“
        把不同种类的怪兽中，相同的属性、方法、放在基类”怪兽“内

"""
# ----------------------------------------------------------------------------------------------------
"""
类的继承：
    在面向对象程序设计中类是可以继承的，其中被继承的类称父类(parent class)或基类(base class),
继承的类称子类(child class)或衍生类(derived class).
    类继承的最大优点是许多父类的公有方法或属性，在子类不用重新设计，可以直接引用。
"""


# ----------------------------------------------------------------------------------------------------
# 基类(Base Class)
#   公有属性
#   公有方法

# 衍生类(Derived Class)
#   继承 Base Class公有属性
#   继承 Base Class公有方法
#   自由的属性与方法

# --------------------------------------------------------
class Monster:  # Monster 怪兽
    # 属性
    def __init__(self):
        pass

    @staticmethod
    def shout():  # shout 喊叫 ； method 方法
        print("angry")


class FlyMonster(Monster):
    @staticmethod
    def fly():
        print("I'm flying")


class SwimMonster(Monster):
    @staticmethod
    def swim():
        print("I'm swimming")


class SpeedMonster(Monster):
    @staticmethod
    def run():
        print("I'm running")


goblins = Monster()
goblins.shout()

bruker = FlyMonster()
bruker.shout()
bruker.fly()

tanuki = SwimMonster()
tanuki.shout()
tanuki.swim()

plushToy = SpeedMonster()
plushToy.shout()
plushToy.run()


# ----------------------------------------------------------------------------------------------------
# 如何取得基类的私有属性？
#   基于保护原因，类外是无法直接取类内的私有属性，即使是它的衍生类也无法直接读取。
#   如果要读取，可以使用 return方式传回私有属性的内容。

# ------------------------------------------
# 衍生类与基类有相同名称的[属性]，也可以有自己的初始化 __init__()方法，同时也有可能衍生类的属性与方法名称和基类重复。
# 衍生类与基类有相同名称的[方法]，也可以有自己的方法，同时也有可能 衍生类的方法名称 与 基类的方法名称重复。

# ------------------------------------------
# 衍生类引用基类的方法 super()
class Animals:
    """Animals类，这是基类"""

    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age

    def run(self):
        print(self.name.title(), "is running")


class Dogs(Animals):
    """Dogs类，Animal的衍生类"""

    def __init__(self, dog_name, dog_age):
        super().__init__("My pet" + dog_name.title(), dog_age)


myCat = Animals("lucy", 5)
print(myCat.name.title(), 'is', myCat.age, "years old.")


# ------------------------------------------
# super()方法____对于三代同堂设计是重要的（grandfather,father,ivan）

# 兄弟类属性的取得
#   假设一个 Father类有 2个儿子，分别是 Ivan,Ira。Ivan类想取得 Ira的属性

class Father:
    """定义父类的资产"""
    def __init__(self):
        self.Father_asset = 10000


class Ira(Father):
    """定义子类的资产"""

    def __init__(self):
        self.Ira_asset = 8000
        super(Ira, self).__init__()


class Ivan(Father):
    def __init__(self):
        self.Ivan_asset = 3000
        super(Ivan, self).__init__()

    def get_money(self):    # 取得资产明细
        print("Ivan资产：", self.Ivan_asset,
              "\nFather资产：", self.Father_asset,
              "\nIra资产：", Ira().Ira_asset)      # 注意写法


ivan = Ivan()
ivan.get_money()


# 类 —— 面向对象的程序设计
"""
    python其实是一种面向对象的编程(Object Oriented Programming),在 python中其实所有的数据类型皆是对象。
python也允许程序设计师自创数据类型，这种自创的数据类型就是  类 (Class)。
    设计程序时候可以将世间万物分组归类，然后用类(class)定义分类。
"""

# -----------------------------------------------------------------------------------------------
# 类的概念与特征
"""
类:
     一种面向对象语言的 程序设计 中的概念，是 面向对象编程 的基础。
     实质:
            一种引用数据类型 ，类似于 byte 、 short 、 int (char)、
            long 、 float 、 double 等基本数据类型，
            不同的是它是一种复杂的数据类型。
            因为它的本质是 数据类型 ，而不是 数据 ，
            所以不存在于内存中，不能被直接操作，
            只有被实例化为对象时，才会变得可操
            # 类是对现实生活中一类具有共同特征的事物的抽象
            
类的三大特性:
    封装性：
        将数据和操作封装为一个有机的整体。
        由于类中私有成员都是隐藏的，只向外部提供有限的接口，所以能够保证内部的高内聚性和与外部的低耦合性。
        用者不必了解具体地实现细节，而只是要通过外部接口，以特定的访问权限来使用类的成员，能够增强安全性和简化编程。
    继承性：
        更符合认知规律，使程序更易于理解，同时节省不必要重复代码。
    多态性：
        是指同一操作作用于不同对象，可以有不同的解释，产生不同的执行结果。
        在运行时，可以通过指向父类（基类）的指针，来调用实现子类（派生类）中的方法。

类与类之间的关系：
    1.继承
        指能够直接获得已有的性质和特性，而不必重复定义它们。
        在面向对象的软件技术中，继承是子类自动的共享父类中的定义的数据和方法的机制。
    2.多态性
        指在父类中定义的属性或操作，被子类继承后，可以具有不同的数据类型或表现出不同的行为。
    3.关联
        关联是两个类之间的强依赖关系，具有长期性，关联可以是单向的，也可以是双向的。
    4.依赖
        一个类使用到另一个类，具有临时性。
    5.实现
        用来规定接口和实现接口的类之间的关系，接口是操作的结。
    6.聚集和组合：
        表示整体和部分之间的关系，组合与聚集是不同的。
"""

# 定义类
'''
class Banks:
    # 定义银行类别
    title = 'China Bank'  # 定义属性

    def motto(self):  # 定义方法
        return "客户至上"
'''


# -----------------------------------------------------------------------------------------------
# 操作类的属性与方法 —————————— 类的构造函数
# 首先要定义该类的对象(object)变量，可以简称对象。
#       object.类的属性
#       object.类的方法()

# 建立类很重要的一个工作是[初始化]整个类.
# 初始化（构造函数）：
#       [__init__()]     init： initialization 初始化 缩写
#   所谓初始化类是在类内建立一个初始化方法(method),这是个特殊的方法，挡在程序内定义这个类的对象时将自动执行这个方法。


class King:  # kind 类
    # 自定义添加属性参数，初始化方法
    def __init__(self, name, weight, height):  # 当只有一个参数 self时，调用时可以不用任何参数
        # 初始化必须包含 self对象参数
        print("--准备初始化--")
        self.name = name  # 设定 name 属性
        self.weight = weight  # 设定 weight 属性
        self.height = height  # 设定 height 属性
        print("--初始化结束--")

    # 自定义类的方法，被对象调用
    def kill(self):
        # 实例方法，必须包含self参数
        print("let's go!!!")
        # 方法---------操作


my = King("YanBin", 62, 179)  # 定义对象 King
my.kill()  # 类的方法
print("我是:", my.name)
print("我的体重:", my.weight)
print("我的身高:", my.height)

# -----------------------------------------------------------------------------------------------
# 属性初始值的设定
"""
设定开户（定义Banks类对象）只要姓名，同时设定开户金额0元。
"""

"""
class Banks:
    # 定义银行类
    def __init__(self, name):  # 初始化方法
        self.name = name  # 设定存款人姓名
        self.balance = 0  # 设定开户账户初始金额 ; balance 平衡，余额
        self.title = 'China Banks'  # 设定银行名称

    # 设计存款方法
    def save_money(self, money):
        self.balance += money
        print(f"存款{money}完成")

    # 设计取款方法
    def withdraw_money(self, money):
        self.balance -= money
        print(f"取款{money}完成")

    # 显示存款金额
    def show_balance(self):
        print(f"{self.name.title()},目前金额{self.balance}")


Pear_bank = Banks('Pear_pay')  # 定义对象 Pear_bank
print("开户银行：", Pear_bank.title)
Pear_bank.save_money(1000)
Pear_bank.withdraw_money(200)
Pear_bank.show_balance()
"""

# -----------------------------------------------------------------------------------------------
# 私有属性
"""
class Banks:
    # 定义银行类
    def __init__(self, name):  # 初始化方法
        self.__name = name  # 设定存款人姓名
        self.__balance = 0  # 设定开户账户初始金额 ; balance 平衡，余额
        self.__title = 'China Banks'  # 设定银行名称

    # 设计存款方法
    def save_money(self, money):
        self.__balance += money
        print(f"存款{money}完成")

    # 设计取款方法
    def withdraw_money(self, money):
        self.__balance -= money
        print(f"取款{money}完成")

    # 显示存款金额
    def show_balance(self):
        print(f"{self.__name.title()},目前金额{self.__balance}")


apple_bank = Banks('apple')
apple_bank.show_balance()
apple_bank.balance = 100        # 私有化后，无法直接篡改存款金额
apple_bank.show_balance()
"""


# -----------------------------------------------------------------------------------------------
# 私有方法
#   观念于私有属性类似，类外的程序无法调用。定义方式与私有属性相同。
class Banks():
    def __init__(self, name):  # 初始化方法
        self.__name = name  # 设定私有存款者名字
        self.__balance = 0  # 设定私有开户金额
        self.__title = "China banks"  # 设定银行名称
        self.__rate = 6.68  # 预设美金兑人民币汇率
        self.__service_charge = 0.01  # 换汇的服务率

    def save_money(self, money):
        self.__balance += money
        print(f"存款{money}完成")

    def withdraw_money(self, money):
        self.__balance -= money
        print(f"取款{money}完成")

    def get_balance(self):
        print(self.__name.title(), "目前金额", self.__balance)

    def us_to_ch(self, u_c):
        self.result = self.__cal_rate(u_c)
        return self.result

    def __cal_rate(self, u_c):
        return int(u_c * self.__rate * (1 - self.__service_charge))


china_bank = Banks('pear bank')
dollar = 50
print(dollar, "美金可以兑换", china_bank.us_to_ch(dollar), "人民币")

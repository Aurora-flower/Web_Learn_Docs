# 多态(多型 polymorphism)

# ----------------------------------------------------------------------------------------------------
# 继承：子类继承了基类的方法
# 多态基础：子类执行多态方法
# 多态进阶：增加新的子类


# 关注点：
# 1     子类继承了基类的方法，无需忍耐和操作得到了基类的方法
# 2     子类执行多态方法
# 3     构造一个调用基类的方法A，增加新子类，同样能使用方法A

# ----------------------------------------------------------------------------------------------------
class Monster:
    def __init__(self):  # attack 攻击，skill 技能
        print("-----初始化开始---")
        # self.name = name
        # self.attack = attack
        # self.skill = skill
        print("-----初始化结束---")

    def attack(self):
        print("attack:punch")  # 定义基本技能：挥拳punch

    def skill(self):
        print("skill: run")


class MonsterA(Monster):
    def attack(self):  # 定义攻击方式有咬人bite
        print("bite")

    def skill(self):
        print("suicide")


class MonsterB(Monster):
    def attack(self):  # 定义攻击方式有喷火Spitfire
        print("Spitfire")

    def skill(self):
        print("suicide")


class MonsterC(Monster):
    def attack(self):  # 定义攻击方式有砍chop
        print("chop")

    def skill(self):
        print("suicide")


# White black red
white = MonsterA()
white.attack()


# 多态理解：不同对象，使用同样的方法，得到的结果是不同的
# --------------------------------


class People:
    def speak(self):
        print("hello!")


class Teacher(People):
    pass


class Student(People):
    pass
    # print("------")


# 该处的 pass 是占据一个位置，
# 如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。


def start_talk(people):
    print("-----准备发言-----")
    people.speak()
    print("-----结束发言-----")


me = Teacher()
# me.talk()
start_talk(me)
print(isinstance(me, Student))  # isinstance(A, B)   判断A是否属于B


# ----------------------------------------------------------------------------------------------------
# 多重继承
#   在面向对象的程序设计中，也常有一个类继承多个类的应用，此时子类也同时 继承了多个类的方法。
#   class 类名称(父类 1,父类 2, ...)
#       类内容
class Grandpa:
    """定义祖父类"""
    def action_one(self):
        print("GrandFather")


class Father(Grandpa):
    """定义父亲类"""
    def action_two(self):
        print("Father")


class Uncle(Grandpa):
    """定义叔叔类"""
    def action_two(self):   # 2
        print("Uncle")


class Ivan(Father,Uncle):
    """定义Ivan类"""
    def action_three(self):  # 3
        print("Ivan")


ivan = Ivan()
ivan.action_three()   # 顺序 Ivan
ivan.action_two()   # 顺序 Ivan -> Father
ivan.action_one()   # 顺序 Ivan -> Father -> Grandfather

# ------------------------------------------------
# type 与 isinstance  (instance 实例)

# type再现
print("Ivan的action_three类型",type(Ivan.action_three))

# isinstance()函数可以传回对象的类是否属于某一类
# 它包含两个参数，语法如下：
#   isinstance(对象,类)
#   如果对象的类属于第 2个参数类，或属于第二个参数的子类则传回 True，否则传回 False.

print("判断：",isinstance(Ivan,Uncle))

# ------------------------------------------------
"""
class Grandpa:
    '''定义祖父类'''
    def action_one(self):
        print("GrandFather")


class Father(Grandpa):
    '''定义父亲类'''
    def action_two(self):
        print("Father")


class Uncle(Grandpa):
    '''定义叔叔类'''
    def action_three(self):     # 3
        print("Uncle")


class Ivan(Father,Uncle):
    '''定义Ivan类'''
    def action_four(self):      # 4
        print("Ivan")


ivan = Ivan()
ivan.action_three()   # 顺序 Ivan
ivan.action_two()   # 顺序 Ivan -> Father
ivan.action_one()   # 顺序 Ivan -> Father -> Grandfather
"""
# ----------------------------------------------------------------------------------------------------

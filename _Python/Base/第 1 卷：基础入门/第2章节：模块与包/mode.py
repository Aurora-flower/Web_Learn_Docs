# 自定义模块 Customized Modules

# 在 [document_name] 文件内定义模块:
# def test():
#     print("hello world")

# 在主体文件中引用
#   import Modules(document name)
#   Modules.text()

# -----------------------------------------------------------------------------------------------------
import math
import os


def ride(variable):
    value = variable ** 2
    print(value)


def study():
    # 控制这两种情况执行代码的过程:
    if __name__ == '__main__':
        # 1.即文件作为脚本直接执行
        print("自我调用")
    else:
        # 2.引进 (import) 到其他脚本中是不会被执行的
        print("被动调用")


def circular_area(radius):
    mark = round(math.pi, 2)  # 保留两位小数
    circle = radius * mark
    print(circle)


def rectangle_area():
    length = int(input("Please enter the length:"))
    width = int(input("Please enter the width:"))
    calculation = length * width
    print(calculation)


# -----------------------------------------------------------------------------------------------------
# import os
print('在 a.py 文件中 %s' % id(os))

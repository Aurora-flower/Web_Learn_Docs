# 导入:
#   from/import的使用  (部分导入)/(全部导入)
#       import 模块名称
import mode
import mode as module
from mode import study as learn

"""
    一个大型程序一定是由许多的函数或类所组成,为了让程序的工作可以分工以及增加程序的可读性,我们可以将所建
的函数或类存储称模块(module)形式的独立文件,未来再加以引用.
"""
# 也可以在模块内导入另一个模块的类
# ----------------------------------------------------------------------------------------------------------
# 调用自定义模块  Invoke Customized Modules

# 导入模块内特定单一函数
#    from 模块名称 import 函数名称
from mode import study
from mode import circular_area
from mode import rectangle_area

# 程序中要引用模块中的函数,语法如下:
#   模块名称.函数名称[1,2,3.....]   (模块名称与函数名称之间有小数点,可以导入模块内多个函数)
# 导入模块内所有函数:
#   from 模块名称 import *
var = mode.ride(3)
study()
circular_area(3)
rectangle_area()

# ----------------------------------------------------------------------------------------------------------
# {as 的作用}

# 1.使用 as 给函数指定替代名称
'''
    有时所设计程序的函数名称与模块内的函数相同,或是感觉模块的函数名称太长,此时可以自行给模块的函数
名称设置一个[替代名称],未来可以使用替代名称代替原先模块的名称.

语法:
    from 模块名称 import 函数名称 as 替代名称
'''
# from mode import study as learn

learn()  # study = learn

# 2.使用 as 给模块指定替代名称
'''python也允许给模块指定名称,格式 [import 模块名称 as 替代名称]'''
# import mode as module

module.circular_area(2)

# ----------------------------------------------------------------------------------------------------------



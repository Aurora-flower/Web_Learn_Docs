# 函数概念
#   所谓的函数（function）其实就是一系列的指令语句组成。

"""
函数概念：
    凡此变量中函（包含）彼变量者，则此为彼之函数；

    * 函：    包含；盒子
    * 黑盒：  标准函数、内置函数、第三方函数；  （绝对值 absolute）
    * 白盒：  自定义函数   （ x if x>0 else -x)

 """

# ---------------------------------------------------------------------------------------
# 从不同的角度解析函数是什么及其分类。（费曼技巧）

"""
    目的：
        1.程序简单化，易查错；分工撰写，缩短开发时间
            当我们在设计一个大型程序时，若能将这个程序依功能，将其分割成较小的功能，然后根据这些较小功能要求撰写函数程序。
        如此，不仅使程序简单化，最后程序侦错也变得容易。另外，撰写大型程序时应该是团队合作，每个人负责一个小功能，可以缩短开发时间。
        2.减少重复程序
            在一个程序中，也许会发生某些指令被重复书写在不同的地方，若是我们能将这些重复的指令撰写成为一个函数，
        需要时再加以调用。如此，不仅减少编辑程序的时间，更可使程序精简、清晰、明了。

    定义：
        语法格式：
            def 函数名称(参数):
            '''函数批注'''
                程序代码区块
                return(返回值)
        *   函数名称：       名称必须是唯一的，程序未来可以调用。
        *   参数值：        可有可无，完全视函数设计需要，可以接收调用函数传来的变量，各参数值之间是用逗号分隔。
        *   函数批注：       可有可无，当参与大型程序设计时，负责一个小程序时，建议批注，方便自己和他人阅读。
        *   return[返回值]：  return和返回值皆可有可无。多个返回值，逗号分隔。
        
    分类:
        内置函数：
            (built-in function)  python自身带有的，实践中使用非常频繁的一些函数；
        自定义函数：
            (custom function)  通常是指，程序员自己在使用的函数；
        模块函数： 
            (modularity function) 把一些函数，单独放在被称为模块的文件中，这些函数就被称为模块函数。
    这些函数可能是python自带的，也可能是由第三方开发的函数。
"""
# ---------------------------------------------------------------------------------------
# 局部变量和全局变量

'''
局部变量:
    某个变量只有在该函数内使用,影响范围限定在这个函数内,这个变量称局部变量(local variable).
全局变量:
    某个变量的影响范围是在整个程序,则这个变量称为全局变量(global variable).
    
概述：
    python程序在调用函数时会建立一个内存工作区间,这个内存工作区间可以处理属于这个函数的变量,
当函数工作结束,返回原先调用程序时,这个内存工作区间就被收回,原先存在的变量也被销毁,这也是为何
局部变量的影响范围只限定在所属函数内.
    对于全局变量而言,一般是在主程序建立,程序在执行时,不仅主程序可以引用,所有属于这个程序的函数
    可以引用,所以它的影响范围是整个程序.
    
总结：
    * 在函数外边定义的变量叫做全局变量
    * 全局变量能够在所有的函数中进行访问
    * 如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
    * 如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的。
'''


# ----------------------------------------------------
# 全局变量可以在所有函数使用
#   一般在主程序内建立的变量称全局变量.这个变量程序内与本程序内的所有函数皆可以引用
def printmsg():
    # 函数本身没有定义变量，只有打印全局变量功能
    print("函数打印：", msg)


msg = "Global variable"
print("主程序打印:", msg)
printmsg()

# ----------------------------------------------------
# 局部变量与全局变量使用相同的名称

# ----------------------------
#   python语言中：
'''
    python会将相同名称的区域与全局变量视为不同的变量，在局部变量所在的函数是使用局部变量内容，
其他区域则是使用全局变量的内容。
'''

# ----------------------------
#   C语言中：
'''
问题：局部变量是否能和全局变量重名？ 
答：能，局部会屏蔽全局。要用全局变量，须要使用"::"
    局部变量能够与全局变量同名，在函数内引用这个变量时，会用到同名的局部变量，而不会用到全局变量。
对于有些编译器而言，在同一个函数内能够定义多个同名的局部变量，比方在两个循环体内都定义一个同名的局
部变量，而那个局部变量的作用域就在那个循环体内。
'''

# ----------------------------
# 局部变量与全局变量定义了相同的变量
"""
def printmsg():
    # 函数本身有定义变量，将打印局部变量功能
    msg = 'Local variable'
    print("函数打印：", msg)


msg = "Global variable"
print("主程序打印:", msg)
printmsg()
"""

# ----------------------------------------------------
# 程序设计需要注意事项：
#   局部变量内容无法在其他函数引用
#   局部变量无法在主程序引用



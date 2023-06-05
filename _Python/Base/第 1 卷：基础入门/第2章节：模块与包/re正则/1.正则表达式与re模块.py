# 什么是正则表达式？
#   通俗理解，按照一定的规则，从某个字符串中匹配出想要的数据。
import re

# 参考：
"""
    正则表达式，又称规则表达式。（英语：Regular Expression，在代码中常简写为 regex、regexp或 RE），计算机科学的一个概念。
正则表达式通常被用来检索、替换那些符合某个模式(规则)的文本。
    许多程序设计语言都支持利用正则表达式进行字符串操作.
"""

# ---------------------------------------------------------------------------------------
# 正则表达式语法：
'''
    * 单字符串匹配规则
    * 匹配多个字符串
    * 开始结束和或语法
    * 转义字符和原生字符串
'''

# ---------------------------------------------------------------------------------------
# 匹配某个字符
text_one = 'ban smoke'
ret_one = re.match('ban', text_one)
print(ret_one.group())

# ---------------------------------------------------------------------------------------
# 点(.): 匹配任意字符(除了'\n')
text_two = 'define'
ret_two = re.match('.', text_two)
print(ret_two.group())

# ---------------------------------------------------------------------------------------
# \d：匹配任意的数字
text_three = '1 years old'
ret_three = re.match("\d", text_three)
print(ret_three.group())

# \D：匹配任意的非数字
text_four = 'ten'
ret_four = re.match("\D", text_four)
print(ret_four.group())

# ---------------------------------------------------------------------------------------
# \s：匹配的是空白字符（包括：\n，\t，\r和空格）
text_five = '  cookie '
ret_five = re.match("\s", text_five)
print('=' * 20)
print(ret_five.group())
print('=' * 20)

# \S：非空白字符
text_six = 'web'
ret_six = re.match("\S", text_six)
print(ret_six.group())

# ---------------------------------------------------------------------------------------
# \w：匹配的是 a-z 和 A-Z 以及数字和下划线
text_seven = 'draw'
ret_seven = re.match("\w", text_seven)
print(ret_seven.group())

# \W：匹配的是和 \w相反的
text_nine = '+ pull'
ret_nine = re.match("\W", text_nine)
print(ret_nine.group())

# ---------------------------------------------------------------------------------------
# []组合的方式，只要满足中括号中的某一项都算匹配成功
text_ten = 'organize'
ret_ten = re.match("[org]", text_ten)
print(ret_ten.group())

# ---------------------------------------------------------------------------------------
# 使用组合的方式[0-9]\d
text_eleven = '012345 combination '
ret_eleven = re.match("[0-9]", text_eleven)
print(ret_eleven.group())

# 使用组合的方式[0-9]\D
text_eleven = 'combination '
ret_eleven = re.match("[^0-9]", text_eleven)  # ^ 取反
print(ret_eleven.group())

# ---------------------------------------------------------------------------------------
# 使用组合的方式实现\w
text_twelve = 'realization 实现'
ret_twelve = re.match("[a-z]", text_twelve)
print(ret_twelve.group())

# 使用组合的方式实现\W
text_thirteen = 'Reality 现实'
ret_thirteen = re.match("[^a-z]", text_thirteen)
print(ret_thirteen.group())

# ---------------------------------------------------------------------------------------
# ^:


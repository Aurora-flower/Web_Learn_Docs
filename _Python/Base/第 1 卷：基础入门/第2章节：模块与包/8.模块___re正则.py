"""
概念：
    re -- 又称规则表达式;
    Regular expression，常简写为regex，regexp或RE;
    常被用来检索、替换那些符合某个模式(规则)的文本.

使用：
    对字符串操作的逻辑
    用定义好的特定字符组成
    ‘规则’字符串
    规则字符串用来表达对字符串的一种逻辑

作用：
    验证数据的有效性
    替换文本内容
    从字符串中提取子字符串
    爬虫
"""

import re

parameter = "动态参数，dynamic parameter"
print(re.search('，', parameter))
# search(pattern,string)
# 搜寻(模式,字符串)， 在字符串中寻找模式

character = "dell 灵越14-5488，i7处理器"
print(re.match("dell", character))
# match(pattern,string)
# 匹配(模式,字符串)，在字符串开始匹配模式

string = "现代海力士(SK) 笔记本内存，规格ddr4 8g 2666"
print(re.split("，", string))  # 区分中英文逗号
# split（pattern,string)
# 分割(模式,字符串)，根据模式分割字符串

print(re.findall('[Gg]', string))
# findall(pattern,string)
# 查找所有(模式，字符串），列表形式返回匹配项

model = re.compile('[0-9]')
mode = "距离考试还有最后8天"
print(re.match('.', mode).group())

# compile(pattern)
# 编写(模式),创建模式对象

# [aeiou]     匹配中括号内的任意一个字母
# [0-9]       匹配任何数字
# [a-z]       匹配任何小写字母
# [A-Z]       匹配任何大写字母
# [a-zA-Z0-9] 匹配任何字母及数字
# [^aeiou]    匹配除了aeiou以外所有的字符
# [^0-9]      匹配除了数字外所有的字符
# [Py]python 学习  匹配"python 学习"或"Python"

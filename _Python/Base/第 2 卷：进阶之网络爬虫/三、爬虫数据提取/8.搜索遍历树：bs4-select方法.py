# 搜索遍历树：
#   css选择器的方式可以更加的方便。
#   使用css选择器的语法，应该使用select方法。

# --------------------------------------------
"""
常用的css选择器方法（select方法）：
    1. 通过标签名查找：
        print(soup.select('a'))
    2. 通过类名查找：
        print(soup.select('.sister'))
    3. 通过ID查找：
        print(soup.select('#link1'))
    4. 组合查找：
        print(soup.select('p #link1'))
    5. 通过属性查找：
        print(soup.select('a[href="https://example/.com/eisie"]'))
    6. 获取内容
        print(soup.select('title')[0].get_text())
"""
# ----------------------------------------
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="https://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')

# （1）通过标签名查找：
print(soup.select('a'))
print('\n------------------------------------\n')
# a = soup.select('a')
# print(type(a))   # ResultSet 结果集合

# （2）通过类名查找：
print(soup.select('.sister'))
print('\n------------------------------------\n')

# （3）通过id查找：
print(soup.select('#link1'))
print('\n------------------------------------\n')

# （4）组合查找：
print(soup.select('p #link1'))
print('\n------------------------------------\n')
print(soup.select('head > title'))
print('\n------------------------------------\n')

# （5）通过属性查找：
print(soup.select('a[href="https://example.com/elsie"]'))  # 同一属性，不能有空格
print('\n------------------------------------\n')

# （6）获取内容：
print(soup.select('title')[0].get_text())   # 列表下标取值

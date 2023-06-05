# BeautifulSoup4库
# 同lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器，主要的功能是如何解析和提取 HTML/XML 数据。

# --------------------------------------------
# # BeautifulSoup4  lxml  re正则
# 比较：
# lxml 只会局部遍历，而Beautiful Soup 是基于HTML DOM（Document Object Model）的，
# 会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml。

# 解析速度:
#     BeautifulSoup4 < lxml < re正则

# 使用难度:
#     BeautifulSoup4 > lxml > re正则
# --------------------------------------------
# 安装：
# pip install bs4

# 中文文档：'https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html'
# --------------------------------------------
# 简单使用
from bs4 import BeautifulSoup
# 创建 Beautiful Soup 对象
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="https://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 使用lxml来进行解析,完善html
# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象
# soup = BeautifulSoup(html,'lxml')
soup = BeautifulSoup(html)

# prettify = pretty 美化,漂亮的
# prettify() 用来实现格式化输出,可以用于BeautifulSoup对象也可以用于任何标签对象
print(soup.prettify())

# --------------------------------------------


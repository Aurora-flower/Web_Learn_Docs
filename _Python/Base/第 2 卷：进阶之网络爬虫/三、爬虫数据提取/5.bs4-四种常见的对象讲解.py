# --------------------------------------------
# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象
# 常见的四种对象:
# 1. Tag：
#       BeautifulSoup中所有的标签都是Tag类型，
#       并且BeautifulSoup的对象其实本质上也是一个Tag类型。
#       所以其实一些方法比如find、find_all并不是BeautifulSoup的，而是Tag的。
#       Tag 通俗点讲就是 HTML 中的一个个标签。
#       我们可以利用 soup 加标签名轻松地获取这些标签的内容，这些对象的类型是bs4.element.Tag。
#       注意，它查找的是在所有内容中的第一个符合要求的标签
# 2. NavigableString：
#       继承自python中的str，用起来就跟使用python的str是一样的。
#       bs4.element.NavigableString 类：表示 HTML 中标签的文本。
#       如果拿到标签后，还想获取标签中的内容。那么可以通过tag.string获取标签中的文字。
# 3. BeautifulSoup：
#       继承自Tag。用来生成BeautifulSoup树的。
#       对于一些查找方法，比如find、select这些，其实还是Tag的。
#       BeautifulSoup 对象表示的是一个文档的全部内容.
#       大部分时候,可以把它当作 Tag 对象,它支持 遍历文档树 和 搜索文档树 中描述的大部分的方法
# 4. Comment：
#       这个也没什么好说，就是继承自NavigableString。
#       Comment 对象是一个特殊类型的 NavigableString 对象.
#       Tag , NavigableString , BeautifulSoup 几乎覆盖了html和xml中的所有内容,
#       但是还有一些特殊对象.容易让人担心的内容是文档的注释部分
# --------------------------------------------

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
<e><!--hey,buddy.want to buy a used parser? --></e>
"""
# 使用lxml来进行解析,完善html
soup = BeautifulSoup(html,'lxml')

# print(soup)
print(type(soup))  # <class 'bs4.BeautifulSoup'> Beautiful Soup 对象

# ---------------------------
# prettify = pretty 美化,漂亮的
# prettify() 用来实现格式化输出,可以用于BeautifulSoup对象也可以用于任何标签对象
# print(soup.prettify())
# print(type(soup.prettify()))

# ---------------------------
# 找到html中的第一个<p>标签
print(soup.p)
print(type(soup.p))  # <class 'bs4.element.Tag'>

# ---------------------------
# bs4.element.Tag 类：
#   Tag对象
#   表示 HTML 中的标签，是最基本的信息组织单元，它有两个非常重要的属性，
#   分别是表示标签名字的 name 属性和表示标签属性的 attrs 属性.
print(soup.p.name)
print(soup.p.attrs)   # 返回值为字典型

# ---------------------------
# 获取<p>标签下的class属性
print(soup.p['class'])
print(soup.p.get('class'))

# replace替换<p>标签下的class属性
soup.p['class'] = 'new'
print(soup.p)

# --------------------------------------------
# from bs4.element import NavigableString
print(soup.p.string)
print(type(soup.p.string))  # <class 'bs4.element.NavigableString'>

print(soup.e.string)
print(type(soup.e.string))

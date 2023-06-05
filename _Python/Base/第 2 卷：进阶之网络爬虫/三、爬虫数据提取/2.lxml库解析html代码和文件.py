# lxml库：
#       HTML/XML的解析器，主要的功能是如何解析和提取 HTML/XML 数据。
# from lxml import etree

# ---------------------------------------------------------
# 基本使用：
#       用来解析HTML代码，并且在解析过程中，如果HTML代码不规范，会自动进行补全。
"""
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
print(result)
"""
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>    
         <!--未闭合-->
     </ul>
 </div>
'''
# 将字符串解析为html文档
html = etree.HTML(text)
print(html)
# 按字符串序列化html
result = etree.tostring(html).decode('utf-8')
print(result)

# ---------------------------------------------------------
# 读取
# 除了直接使用字符串进行解析，lxml还支持从文件中读取内容。
"""
html = etree.parse('[html--文件名]')
result = etree.tostring(html).decode('utf-8')
print(result)
"""
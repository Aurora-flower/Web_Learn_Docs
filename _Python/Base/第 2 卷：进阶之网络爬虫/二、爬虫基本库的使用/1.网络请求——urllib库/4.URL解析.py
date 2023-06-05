# urlparse(parameter-6)和urlsplit(parameter-5):
#       对url中各个组成部分进行分割。

# 区别：urlparse里有params属性，而urlsplit没有该属性

# ------------------------------------------
from urllib import parse

url = 'https://www.aspxfans.com:8080/news/index.asp?boardID=5&ID=24618&page=1#name'

# result = parse.urlparse(url)    # ParseResult-6
result = parse.urlsplit(url)    # ParseResult-5
print(result)
print(result.scheme)  # 可以单独打印所需要的属性值

# ------------------------------------------
# ParseResult:
#       scheme    协议
#       netloc    域名
#       path      路径
#       params    参数
#       query     查询条件
#       fragment  锚点


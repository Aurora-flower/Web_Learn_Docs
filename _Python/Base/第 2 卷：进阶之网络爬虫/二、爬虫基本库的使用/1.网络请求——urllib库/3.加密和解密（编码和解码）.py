# urllib库的parse模块(module)

# parse -  v.（对句子）作语法分析；作句法分析;  解析；剖析；分析语句

# -----------------------------------------------------
# encode编码:
#       urlencode函数————可以把字典数据转换为URL编码的数据。

# 编码原因reason：
#       url中不能含有中文，需要转码.

# -----------------------------------------------------
from urllib import parse

# data = {'name': '爬虫基础', 'greet': 'hello world', 'age': 100}
data = {'Web page encoding': '进行编码的中文'}
page_encode = parse.urlencode(data)
print(page_encode)


# 对字符串的编码 —— parse.quote
char = '字符串'
wd = parse.quote(char)
print('对字符串的编码:', wd)

# ------------------------------------------
# decode解码:
#       parse_qs函数 ———— 可以将经过的编码后的url参数进行编码。

print(parse.parse_qs(page_encode))

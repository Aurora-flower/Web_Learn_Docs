import json

# -------------------------------------------------------------------------------------
# 将 Python对象 [转储(dump)] 成JSON字符串:

# dumps函数：
#   把 Python对象转换成JSON格式的字符串。
books = [
    {
        "title": "钢铁是怎样练成的",
        "price": 9.8
    },
    {
        "title": "红楼梦",
        "price": 9.9
    }
]  # 这里是python对象，可以单引号

json_str = json.dumps(books, ensure_ascii=False)  # ASCII码参数
print(json_str)
print(type(json_str))
# -------------------------------------------------------------------------------------
# dump函数：
#   把 Python对象转换成 JSON格式的字符串，并且还可以接收一个文件指针 fp参数，可以写入到文件中。
"""
    json模块中除了dumps函数，还有一个dump函数，这个函数可以传入一个文件指针，直接将字符
串dump到文件中。
    因为json在dump的时候，只能存放ascii的字符，因此会将中文进行转义。"ensure_ascii"参数，
默认情况下这个参数的值是True，这时候我们可以使用ensure_ascii=False关闭这个特性。
    在Python中，只有基本数据类型才能转换成JSON格式的字符串。即：(int)、(float)、(str)、
(list)、(dict)、(tuple)。
"""
# 示例代码如下：
fp = open("books.json", 'w', encoding='utf-8')
json.dump(books, fp, ensure_ascii=False)

# -------------------------------------------------------------------------------------
# 将 JSON字符串 [负荷(load)]成 Python对象:

# loads：
#   将 JSON字符串转换成 Python对象。

# 示例代码如下：
result = json.loads(json_str)
print(result)
print(type(result))

# -------------------------------------------------------------------------------------
# load：
#   将 JSON字符串转换成 Python对象，并且是直接从文件中获取JSON字符串。

# 示例代码如下：
with open("books.json", 'r', encoding='utf-8') as fp:
    result = json.load(fp)
    print(result)
    print(type(result))

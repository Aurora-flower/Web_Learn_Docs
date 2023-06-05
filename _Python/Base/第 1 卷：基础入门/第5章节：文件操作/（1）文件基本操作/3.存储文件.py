# 文件写入
# 传入标识符‘w’或者‘wb’表示写入文本文件或者写入二进制文件
"""
# 调用open函数时
使用write（）方法的时候，操作系统不是立即将数据写入文件中的，
而是先写入内存中缓存起来，等到空闲时候再写入文件中，
最后使用close（）方法就将数据完整地写入文件中了。

当然也可以使用 f.flush（）方法，不断将数据立即写入文件中，最后使用close（）方法来关闭文件。
"""
# --------------------------------------------------------
from datetime import datetime
# 函数write()
# 写入一个字符或者写入一个字符串
#           f.write("hello!")
file = "lesson1.txt"
with open(file, mode='w', encoding="utf-8") as f:
    f.write("之前老是出错，进行覆盖写入")

with open(file, mode='r+', encoding="utf-8") as f:   # r+: 读写、写入时从头开始覆盖;
    f.write("开头写入替换")

with open(file, mode='w+') as f:   # w+:读写、清空源文件后读写
    f.write('12345678')

# 函数writelines()
# 用于向文件中写入一序列的字符串或字节串，序列可以是列表、元组、字典、集合等；
#        writelines()

with open(file, 'w') as f:
    gf = datetime.strptime("2022/3/21", '%Y/%M/%d')
    # %Y/%M/%d 年/月/日
    result = str("time:"+str(gf.date()))
    f.write(result)
# --------------------------------------------
# 综合练习案例：将一个文本的内容，存入另一个文本

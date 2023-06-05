# -- coding utf-8 --
from urllib import request

# 爬取：遵循robots协议 [scheme://netloc/robots.txt]

# ----------------------------------------------
# 网络请求库：   urllib \ requests

# urllib 库是python中的一个最基本的网络请求库。
# 可以模拟浏览器的行为，向指定的服务器发送一个请求，并可以保存服务器返回的数据。
# 客户端  ——[发送请求] -> 服务端
# 客户端  <- [发送请求] —— 服务端

# urllib与requests的区别：
#                     urllib 内置库
#                     requests 第三方库

# ----------------------------------------------
# urlopen函数：
#           创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据；
#   url:请求的url
#   data:请求的data [若是设置这个参数值，那么将变成post请求]
#   返回值:返回值是一个http.client.HTTPResponse对象，那么这个对象是一个类文件句柄对象。
#         有read(size)、redline、readlines以及getcode等方法.
resp = request.urlopen('https://www.jd.com/')  # 打开网址
# Get HTTPResponse Object's Address

# test
# print(resp)

# ----------------------------------------------
# 读取：
print(resp.read(),end='\n========================\n')  # 获取的全部源代码，是字节型，格式混乱,不易查看
# print(resp.readlin())  # 打印一行
# print(resp.readlines())  # 打印多行
print("状态码 =",resp.getcode())  # 返回状态码，200表示成功

# ----------------------------------------------
# user-agent UA代理获取：
#       快速获取浏览器的User-Agent的方法也很简单，只需要在地址栏中输入：about:version即可

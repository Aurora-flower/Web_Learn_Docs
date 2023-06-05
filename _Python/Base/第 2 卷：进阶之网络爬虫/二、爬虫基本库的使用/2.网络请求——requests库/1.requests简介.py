# Requests：让HTTP服务人类
#     虽然Python的标准库中 urllib模块已经包含了平常我们使用的大多数功能，但是它的
#     API 使用起来让人感觉不太好，而 Requests宣传是 “HTTP for Humans”，说明使
#     用更简洁方便。
#
#     Requests 是用Python语言编写，基于 urllib，但是它比 urllib 更加方便，可以节约我们大量的工作，完全满足 HTTP 测试需求。

# ------------------------------------------------------------------------
# 安装：
#     pip install request

# -------------------------------------
# 发送GET请求：
#       最简单的发送get请求就是通过requests.get来调用：
#       response = requests.get(url)

# -------------------------------------
# 发送POST请求：
#       最基本的POST请求可以使用post方法：
#       response = requests.post(url,data=data)

# -------------------------------------
# 使用代理：
#       使用requests添加代理也非常简单，只要在请求的方法中
#       （比如get或者post）传递proxies(proxy)参数就可以了

# -------------------------------------
# cookie：
#       如果在一个响应中包含了cookie，那么可以利用cookies属性拿到这个返回的cookie值

# import requests
# url = 'https://www.baidu.com/'
# resp = requests.get(url)
# print(resp.cookies)
# print(resp.cookies.get_dict())

# -------------------------------------
# session：
#         使用requests，也要达到共享cookie的目的，那么可以使用requests库给我们提供的
#         session对象。
# 注意：这里的session不是web开发中的那个session，这个地方只是一个会话的对象而已。

# -------------------------------------
# 处理不信任的SSL证书：
#         对于那些已经被信任的SSL证书的网站，比如https://www.baidu.com/，那么使用requests直接就可以正常的返回响应。

# 示例代码如下：
# resp = requests.get('https://inv-veri.chinatax.gov.cn/',verify=False)
# print(resp.content.decode('utf-8'))

# ------------------------------------------------------------------------
# response.text和response.content的区别：

# 1. response.content ：
#     直接从网络上抓取的数据，没有经过任何的编码，是一个bytes类型，
#     在硬盘上和网络上传输的字符串都是bytes类型

# 2. response.text：
#     str的数据类型，是requests库将response.content进行解码的字符串，
#     解码需要指定一个编码方式，requests会根据自己的猜测来判断编码的方式，
#     有时候可能会猜测错误，就会导致解码产生乱码，这时候就应该进行手动解码，
#     比如使用 `response.content.decode('utf-8')`









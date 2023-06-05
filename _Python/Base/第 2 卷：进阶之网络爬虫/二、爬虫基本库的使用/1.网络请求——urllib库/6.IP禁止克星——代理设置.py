# 很多网站会检测某一段时间内，某一IP地址的访问次数(通过流量统计、系统日志等)，
# 如果访问次数多的不像是正常人，会被禁止访问

# -------------------------------------------
# http://httpbin.org/:查看http请求的一些参数
# -------------------------------------------
from urllib import request

# 无代理IP:
url = 'HTTP://httpbin.org/ip'

# notAgent_IP = request.urlopen(url)
# print("无代理下IP",notAgent_IP.read())

# -------------------------------------------
# 使用代理IP:
# Proxy代理 Handler处理器
# 1.使用ProxyHandler，传入代理构建一个handler
protocol = 'http'
ip = ''
port = ''
ip_port = f'{ip}:{port}'
Handler = request.ProxyHandler({protocol:ip_port})

# 2.使用Handler，调用build_opener()构建自定义Opener对象,参数是构建的处理器对象
opener = request.build_opener(Handler)

# 3.opener调用open()方法发送请求
Agent_IP = opener.open(url)

print("有代理下IP",Agent_IP.read())

# -------------------------------------------
# (1)高度匿名代理：
#       会将数据包原封不动的转发，在服务端看来就好像真的是一个普通客户端在访问，而记录的IP则是代理服务器的IP。
#       不改变客户机的请求,这时客户的真实IP是隐藏的，服务器端不会认为我们使用了代理。
# (2)普通匿名代理：
#       会在数据包上做一些改动，服务器上有可能发现这是个代理服务器，也有一定几率追查到客户端的真实IP。
#       能隐藏客户机的真实IP，但会改变我们的请求信息，服务器端有可能会认为我们使用了代理。
# (3)透明代理：不但改动了数据包，还会告诉服务器客户端的真实IP。
# (4)间谍代理：指组织或个人创建的用户记录用户传输的数据，然后进行研究、监控等目的的代理服务器。







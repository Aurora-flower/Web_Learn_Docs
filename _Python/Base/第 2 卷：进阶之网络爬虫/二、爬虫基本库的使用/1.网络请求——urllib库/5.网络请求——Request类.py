# request.Request类的不同：
#       可以携带User-Agent用户代理(IP)、cookie数据等内容进行网址的请求。
#       例如，要求login登录场景的网址

# ------------------------------------------
from urllib import request

url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=17ffa144f270-05bbf87e9fc9d8-4d667e5c-e1000-17ffa144f28c8&timeStamp=1649168423985&User-Agent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMC4wLjQ4OTYuNjAgU2FmYXJpLzUzNy4zNiBFZGcvMTAwLjAuMTE4NS4yOQ%3D%3D&index=220&channelId=40009&sVersion=2&signKey=1738e2c047746874e285887b7193e9a8'

# 设置一个变量，以字典形式存储headers头部信心
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}

# ------------------------------------------
# 设置headers参数，get请求 --> post请求
# post请求: 携带内容对url进行请求
request_webpage = request.Request(url,headers=header)

# ------------------------------------------
# 请求打开对url的post请求，得到Response响应
resp = request.urlopen(request_webpage)

# ------------------------------------------
# 对响应数据进行(decode read)解码读取
print(resp.read().decode('utf-8'))


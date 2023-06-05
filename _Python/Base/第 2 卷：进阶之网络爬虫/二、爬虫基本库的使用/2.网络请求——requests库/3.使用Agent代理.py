import requests

# 使用代理：
#       使用 requests添加代理也非常简单，只要在请求的方法中
#       （比如 get或者post）传递 proxies(proxy)参数就可以了

# -------------------------------------
proxy = {
    'http':'111.77.197.127:9999'
}
url = 'https://www.httpbin.org/ip'
resp = requests.get(url,proxies=proxy)
print(resp.text)

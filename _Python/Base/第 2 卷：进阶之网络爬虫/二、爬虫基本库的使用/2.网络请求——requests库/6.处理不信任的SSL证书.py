import requests

# 处理不信任的SSL证书：
#         对于那些已经被信任的SSL证书的网站，那么使用requests直接就可以正常的返回响应。

# ------------------------------------------------------------------------
resp = requests.get('https://inv-veri.chinatax.gov.cn/',verify=False)
print(resp.content.decode('utf-8'))

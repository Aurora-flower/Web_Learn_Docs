import requests

# 添加headers和查询参数
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

kw = {'wd': '中国'}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要 urlencode()
response = requests.get('https://www.baidu.com/s', headers=headers, params=kw)
#  "url": "https://www.httpbin.org/get?wd=china"

print(response)
# resp = response.text
# print(resp)
# che = ''.join(resp)
# print(che)

# 属性查询响应内容
# print(response.text)        # 返回unicode格式的数据
# print(response.content)     # 返回字节流数据
# print(response.url)         # 查看完整url地址
# print(response.encoding)    # 查看响应头部字符编码

# ------------------------------------------------------------------------

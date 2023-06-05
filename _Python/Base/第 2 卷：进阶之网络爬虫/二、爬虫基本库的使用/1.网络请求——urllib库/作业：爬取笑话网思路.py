from urllib import request

# -------------------------------------------

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',

    'cookie': 'Hm_lvt_371c0214d89fec70079f78acce5c6fc7=1649142381; _ga=GA1.2.487415974.1649142382; _gid=GA1.2.502605644.1649142382; Hm_lpvt_371c0214d89fec70079f78acce5c6fc7=1649142537',

    'referer': 'https://www.biedoul.com/'
}

# 思路：循环遍历的方法进行上下页的切换
for i in range(12360,12363):
    url = 'https://www.biedoul.com/index/'+str(i)
    # print(url)

# 定义Request类请求
    post_request = request.Request(url, headers=header)
    # print(post_request)

# post请求响应地址
    resp = request.urlopen(post_request)
    # print(resp)



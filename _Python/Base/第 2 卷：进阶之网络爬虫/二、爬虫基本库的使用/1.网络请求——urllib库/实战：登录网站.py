# 知乎：

# from urllib import request
#
# url = 'https://www.zhihu.com/hot'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#     'cookie':'_zap=59cde9c3-c5c0-4baa-b756-fa16b5e72b10; d_c0="APDi1NJcuQ6PTvP9qa1EKY6nlhVHc_zYWGM=|1545737641"; __gads=ID=237616e597ec37ad:T=1546339385:S=ALNI_Mbo2JturZesh38v7GzEeKjlADtQ5Q; _xsrf=pOd30ApWQ2jihUIfq94gn2UXxc0zEeay; q_c1=1767e338c3ab416692e624763646fc07|1554209209000|1545743740000; tst=h; __utma=51854390.247721793.1554359436.1554359436.1554359436.1; __utmb=51854390.0.10.1554359436; __utmc=51854390; __utmz=51854390.1554359436.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; __utmv=51854390.100-1|2=registration_date=20180515=1^3=entry_date=20180515=1; tgw_l7_route=537a925d07d06cecbf34cd06a153f671; capsion_ticket="2|1:0|10:1554360474|14:capsion_ticket|44:NDM3YzM4ZjY3MjRkNDJhZGE2ZTFlNDgyYjYzYzhkNWM=|4f72c1edb70a779711a93844e747deb0d7efb6febfd6254d11b3a27844c50a00"; z_c0="2|1:0|10:1554360480|4:z_c0|92:Mi4xOWpCeUNRQUFBQUFBOE9MVTBseTVEaVlBQUFCZ0FsVk5vUGFTWFFCRXZ2bkkzTTNRZk9IVU1NOXFMYXdGNFMwTVB3|769f186a095046f171488c3ba61242ff27bcdef068c2d4cafc6046ff008e1a1a"'
# }
# rq = request.Request(url,headers=headers)
# resp = request.urlopen(rq)
# print(resp.read().decode('utf-8'))

# 始终无反应。
# 猜测：知乎反爬虫机制升级

# ---------------------------------------------------
# ---------------------------------------------------
# 美食杰网：

# http.cookiejar模块方法
from urllib import request,parse
from http.cookiejar import CookieJar


# 登录：https://i.meishi.cc/login.php?redirect=http%3A%2F%2Fi.meishi.cc%2F
# 个人网页 http://i.meishi.cc/?session_id=77852878680850ae4d76480ab9930d1b

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

# ---------------------------------------------------
# 1.登录:
# 1.1 创建cookiejar对象
cookiejar = CookieJar()
# 1.2 使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 使用上一步的创建的handler创建一个opener
opener = request.build_opener(handler)
# 1.4 使用opener发送登录请求  (账号和密码)

post_url = 'https://i.meishi.cc/login.php?redirect=http%3A%2F%2Fi.meishi.cc%2F'
post_data = parse.urlencode({
    'username': '*********',
    'password': '*********'
})
req = request.Request(post_url, data=post_data.encode('utf-8'))
opener.open(req)

# ---------------------------------------------------
# 2.访问个人网页
url = 'https://i.meishi.cc/?session_id=77852878680850ae4d76480ab9930d1b'
rq = request.Request(url, headers=headers)
resp = opener.open(rq)
print(resp.read().decode('utf-8'))

# essay = resp.read().decode('utf-8')
# html = ''.join(essay)
# print(html)
# ---------------------------------------------------


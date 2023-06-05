from urllib import request
from http.cookiejar import MozillaCookieJar

# ---------------------------------------------------------------
# 保存
# 保存cookie到文件，我们需要使用MozillaCookjar()
cookiejar = MozillaCookieJar('cookie.txt')    # 这里加入文件名，save处就不用再添加
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('https://www.httpbin.org/cookies/set/1883/123')

cookiejar.save(ignore_discard=True, ignore_expires=True)

ignore_discard = True  # 即使cookies即将被丢弃也要保存下来
ignore_expires = True  # 如果cookies已经过期也将它保存并且文件已存在时将覆盖

# ---------------------------------------------------------------
# 加载
# cookiejar = MozillaCookieJar('cookie.txt')
# cookiejar.load()  # 加载
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# resp = opener.open('https://www.httpbin.org/cookies/set/course/abc')
#
# for cookie in cookiejar:
#     print(cookie)

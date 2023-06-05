"""
cookie的格式：
    Set-Cookie: NAME=VALUE；Expires/Max-age=DATE；Path=PATH；
    Domain=DOMAIN_NAME；SECURE
"""

# 什么是cookie?
"""        
        指某些网站为了辨别用户身份、进行 session 跟踪而储存在用户本地终端上的数据。
        cookie存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过4KB。
        因此使用cookie只能存储一些小量的数据
"""


# 参数意义：
#     NAME：cookie的名字。
#     VALUE：cookie的值。
#     Expires：cookie的过期时间。
#     Path：cookie作用的路径。
#     Domain：cookie作用的域名。
#     SECURE：是否只在https协议下起作用。

# ------------------------------------------------
# http.cookiejar模块：提供用于存储cookie的对象

"""
http.cookiejar模块主要的类:
        有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

这四个类的作用分别如下:
        1.  CookieJar：
                管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP
                请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾
                回收后cookie也将丢失。

        2.  FileCookieJar (filename,delayload=None,policy=None)：
                从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。
                filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，
                即只有在需要时才读取文件或在文件中存储数据。

        3.  MozillaCookieJar (filename,delayload=None,policy=None)：
            从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

        4.  LWPCookieJar (filename,delayload=None,policy=None)：
            从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实
            例。
"""
import requests

from lxml import etree

import uuid

# UUID 的目的是让分布式系统中的所有元素，都能有唯一的辨识资讯，
# 而不需要透过中央控制端来做辨识资讯的指定。

# 请求，获取源码
url = "https://new.qq.com/omn/20220312/20220312A028AW00.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
}
proxies = {"http": "8.208.91.118:80"}

resp = requests.get(url, headers=headers, proxies=proxies)  # 响应结果是"url"对象,请求进入地址。
# print(resp)   # Response测试

page_source = resp.text  # 将得到的响应对象写成关于源代码的文本
# print(page_source)  # 源代码文本查看

# 加载页面源代码
load_page = etree.HTML(page_source)

# etree.HTML()将写入 text 的字符串转换为 element对象
# 作为_Element对象，可以方便的使用get-parent ()、remove ()、xpath ()等方法。
# print(load_page)  # 元素html测试

# 标题
title = load_page.xpath("//h1/text()")[0]  # 选取列表中第一个元素
# XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。
# print(title)  # 元素html测试

# 正文
mark = load_page.xpath("//div[@class='content-article']")[0]  # 标记限定内容
# print(mark)  # 标记元素测试
thesis = mark.xpath(".//text()")  # 标记点内的（所有）文本
print(''.join(thesis))  # 整理文本格式

# 选择markdown,进行存储
html = etree.tostring(mark, encoding='utf-8').decode('utf-8')  # to string 转换对象为字符串
# 以encoding限定decode解码，将Element对象转字符
# print(html)  # html返回源码测试

# 存储图片，生成本地路径
image_src = mark.xpath(".//img/@src")

# 多个图片的获取需要遍历
for photo_path in image_src:
    downloads_url = "http:" + photo_path  # 路径缺少http协议，进行补充
    print(downloads_url)
    picture_resp = requests.get(downloads_url)
    file_path = f"{uuid.uuid4()}.jpg"
    with open(file_path, mode="wb") as f:
        f.write(picture_resp.content)  # content 内容，对文件写入
    # 当图片下载完毕后，需要更改html中图片的路径
    html = html.replace(photo_path, file_path)  # 改写url路径
#     replace(old,new)

# 写入markdown，自动存储为 .md 文件
with open(f"{title}.md", mode='w', encoding='utf-8') as f:
    f.write(html)

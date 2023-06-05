import time
import uuid
import requests
from lxml import etree
from urllib import request

# from bs4 import BeautifulSoup

# 请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
    "Referer": "https://movie.douban.com/top250?start=225&filter="
}

# 代理IP(未设置)
proxy = {"https": 'ip:port'}


# 解析主页面
def parse_home_url(page_url):
    # 请求过程(用 requests库的 get方法)
    resource = requests.get(page_url, headers=headers)
    page_html = resource.text
    # print(page_html)
    # xpath获取详情页url
    loading_page = etree.HTML(page_html)  # 将 html转换为 element对象
    detail_url_list = loading_page.xpath("//div[@class='hd']/a/@href")
    # 遍历详情页面
    for detail_url in detail_url_list:
        film_url = detail_url
        # print(film_url)  # 测试输出
        # 调取 解析详情页面函数
        detail_page_url(film_url)
        # 设置 rest 控制
        # time.sleep(3)
        break
    # pass


# 解析详情页面
def detail_page_url(film_url):
    # 1.请求页面(下一次用 urllib库的 request类)
    response = requests.get(film_url, headers=headers)
    content = response.text
    detail_html = etree.HTML(content)
    # 2.xpath语法选取内容(下一次用 CSS语法———BeautifulSoup)
    # ---标题
    title = detail_html.xpath("//h1/span[@property='v:itemreviewed']")[0]
    # etree.tostring(title, encoding='utf-8').decode('utf-8')  # 转为字符串

    # ---封面
    cover = detail_html.xpath("//*[@id='mainpic']/a/img")[0]
    # picture_resp = requests.get(cover)
    # ---电影信息
    info = detail_html.xpath("//*[@id='info']")

    # ---剧情介绍
    describe = detail_html.xpath("//div[@class='related-info']")

    # 3.整合内容
    info_list = [title, info, describe]
    for text in info_list:
        context = text
        # 4.保存内容（空列表测试保存文本）
        html = etree.tostring(context, encoding='utf-8').decode('utf-8')
        file_path = f"{uuid.uuid4()}.jpg"
        picture_resp = requests.get(cover)
        with open(file_path, mode="wb") as f:
            f.write(picture_resp.content)
        with open(f"{title}.md", mode='w', encoding='utf-8') as f:
            f.write(html)
        # time.sleep(3)
        break
    # pass


# 主函数
def main():
    # 主页面地址遍历
    for i in range(0, 251, 25):
        domain_url = f'https://movie.douban.com/top250?start={i}&filter='
        # 调用parse_home_url
        parse_home_url(page_url=domain_url)
        # time.sleep(3)
        break
    # pass


# 运行主函数
if __name__ == '__main__':
    main()

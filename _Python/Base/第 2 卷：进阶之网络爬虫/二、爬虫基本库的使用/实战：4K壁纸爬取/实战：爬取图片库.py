# 导入所需的库
import time
import uuid
from urllib import request
import requests
from lxml import etree

# 爬取网页; 4K电脑壁纸
HomePage_url = "https://desk.3gbizhi.com"
# 目标网址： 4K电脑壁纸 —— 动物壁纸
goal_url = "https://desk.3gbizhi.com/deskDM"

# 请求头
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit \
/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
}


# 代理IP
# proxy = {'https': 'ip:port'}


# 解析主页列表
def page_list(page_url):
    response = requests.get(page_url, headers=headers)
    context = response.text
    load_page = etree.HTML(context)
    # print(load_page)
    detail_url_list = load_page.xpath("//ul[@class='cl']/li/a/@href")
    # print(detail_url_list)
    # parse_detail(detail_url_list)
    for url in detail_url_list:
        content_url = url
        request.urlretrieve(url)
        parse_detail(content_url)
        time.sleep(2)
        # break
    # pass


# 解析详情页，选择需要的内容
def parse_detail(content_url):
    resp = requests.get(content_url, headers=headers)
    text = resp.text
    text_parse = etree.HTML(text)
    image = text_parse.xpath(".//img/@src")
    img = ''.join(image)
    # print(img)
    picture_resp = requests.get(img)
    img_path = f"{uuid.uuid4()}.jpg"
    with open(img_path, mode='wb') as f:
        f.write(picture_resp.content)
    print(f"{image}下载完毕！", end='\n')
    # pass


# 主体运行函数
def main():
    for i in range(1, 4):
        page_url = f"https://desk.3gbizhi.com/deskDM/index_{i}.com"
        # print(aim_url)
        page_list(page_url)
        time.sleep(3)


if __name__ == '__main__':
    main()

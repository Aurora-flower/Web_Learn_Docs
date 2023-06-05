import time
import requests
from lxml import etree
from bs4 import BeautifulSoup

# 请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " +
                  "Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
    "Referer": "https://movie.douban.com/top250?start=225&filter="
}

# 代理IP(建议创建代理池模块)
proxies = {"http": "61.133.87.228:55443"}


# 解析主页面
def parse_home_url(page_url):
    # 请求过程(requests库的 get方法)
    home_response = requests.get(page_url, headers=headers, proxies=proxies)
    page_html = home_response.text
    element_page = etree.HTML(page_html)
    # ---获取详情页url---
    page_url = element_page.xpath("//div[@class='hd']/a/@href")
    # print(page_url)  # 列表元素
    for parser_url in page_url:
        info_url = parser_url
        detail_page_url(info_url)
        # continue
        # 设置 rest 控制
        print("正在加载中...请稍后！")
        time.sleep(3)
        # break
    # pass


# 解析详情页面
def detail_page_url(info_url):
    # 1.请求页面(requests)
    data_resp = requests.get(info_url, headers=headers, proxies=proxies)
    info_html = data_resp.text
    element_info = etree.HTML(info_html)

    # ------------xpath方法:获取解析------------
    # ---封面
    cover = element_info.xpath("//a[@class='nbgnbg']/img/@src")[0]
    print(cover)  # 图片 url

    # ----标题----
    title_div = element_info.xpath("//h1")[0]
    title = title_div.xpath('.//text()')
    join_title = ''.join(title).strip().replace(f'\n', '').replace('  ', '')
    # .strip().replace(f'    \n','')
    # print(''.join(title))
    print(join_title)
    # """
    # ----简介----
    info_describe = element_info.xpath("//div[@id='info']")[0]
    # print(info_describe.read().decode('utf-8'))
    info = info_describe.xpath('.//text()')
    join_info = ''.join(info)
    # print(''.join(info))
    print(join_info)

    # ----剧情介绍----
    # thesis_div = element_info.xpath("//div[@class='indent']/span")[1]
    thesis_div = element_info.xpath("//span[@property='v:summary']")[0]
    thesis = thesis_div.xpath('.//text()')
    join_thesis = ''.join(thesis).replace('  ', '')
    # .strip().replace(f'\u3000\u3000','').replace('  ','').replace(f'\n','')
    # # print(''.join(thesis))
    # soup方法：（其实更好用，只是后面需要改动）
    # soup = BeautifulSoup(info_html, 'html.parser')
    # thesis = soup.select("#link-report > span")[0].get_text()
    # print(thesis)
    print(join_thesis)
    # time.sleep(3)

    # """
    # ------------整合内容，进行遍历------------
    # content 内容，对文件写入

    # 图片 content
    # picture_md = requests.get(cover)
    # 标题 content
    title_md = etree.tostring(title_div, encoding='utf-8').decode('utf-8')
    # 简介 content
    info_md = etree.tostring(info_describe, encoding='utf-8').decode('utf-8')
    # 剧情介绍 content
    thesis_md = etree.tostring(thesis_div, encoding='utf-8').decode('utf-8')

    # soup一下，且都转换为字符串
    one_soup = BeautifulSoup(title_md, 'html.parser')
    # print(one_soup)
    title_soup = repr(one_soup)
    two_soup = BeautifulSoup(info_md, 'html.parser')
    info_soup = repr(two_soup)
    # 下面
    three_soup = BeautifulSoup(thesis_md, 'html.parser')
    thesis_soup = repr(three_soup).replace('       ', '')

    # 处理保存照片
    # print(picture_md)
    # with open(f"{join_title}.png", mode='wb') as f:
    #     f.write(picture_md.content)

    # 想到另一种方法：获取标签而不是url
    picture_div = element_info.xpath("//a[@class='nbgnbg']")[0]
    img_md = etree.tostring(picture_div, encoding='utf-8').decode('utf-8')
    # print(img_md)

    # 保存
    with open(f"{join_title}.md", mode='w', encoding='utf-8') as f:
        # f.write(title_md)
        f.write(img_md)

    with open(f"{join_title}.md", mode='a', encoding='utf-8') as f:
        # f.write(title_md)
        f.write(title_soup)
    with open(f"{join_title}.md", mode='a', encoding='utf-8') as f:
        # f.write(info_md)
        f.write(info_soup)
    with open(f"{join_title}.md", mode='a', encoding='utf-8') as f:
        f.write(thesis_soup)
    time.sleep(3)
    # pass


# """


# 主函数
def main():
    # 主页面地址遍历
    for i in range(0, 251, 25):
        domain_url = f'https://movie.douban.com/top250?start={i}&filter='
        # 调用parse_home_url
        parse_home_url(page_url=domain_url)
        print("努力加载中...小主别急！")
        time.sleep(3)
        # break
    # pass


# 运行主函数
if __name__ == '__main__':
    main()
    print("小主，任务完成了！")

# requests对象的 get和 post方法都会返回一个Response对象，
# 这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等。
# 其中返回的网页部分会存在.content和.text两个对象中。
# 两者区别在于，content中间存的是字节码，
# 而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。

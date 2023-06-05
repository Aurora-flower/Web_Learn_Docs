"""
思路：
    多页爬取
    1.define解析网页模块
    2.define解析内容的模块（标题、内容）
    3.main主体运行测试
    4.if判断
"""

import requests
from lxml import etree
import time


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39',
    'cookie': 'ip_ck=4c6G4Pn/j7QuNjk3NzM4LjE2NDk5MzY1MTI%3D; lv=1650084694; vn=2; questionnaire_pv=1650067207'
}

domain_url = 'https://xiaohua.zol.com.cn/'

# 定义容器，全局变量 joke_list()
blank_list = []


# 解析列表页面
def parse_page(page_url):
    # pass
    # ----------------------------------------------------
    # 请求到地址，获取响应，得到源码，Response响应
    resp = requests.get(page_url, headers=headers)
    # ----------------------------------------------------
    # 将得到的响应对象，写成关于源代码的文本
    text = resp.text
    # test:源代码文本查看
    # print(text)
    # ----------------------------------------------------
    # 加载页面源代码
    load_page = etree.HTML(text)
    # test:查看是否解析对象
    # print(load_page)

    # etree.HTML() 将写入 text 的字符串转换为 element对象
    # 作为_Element对象，可以方便的使用get-parent ()、remove ()、xpath ()等方法。
    # ----------------------------------------------------
    # 内容  跳转页面的url获取
    detail_url_list = load_page.xpath("//ul[@class='article-list']/li[@class='article-summary']\
    //a[@class='all-read']/@href")
    # test:url查看
    # print(detail_list_url)
    # ----------------------------------------------------
    # 遍历拼接url
    for detail_url in detail_url_list:
        content_url = domain_url + f'{detail_url}'
        # 调用parse_detail
        parse_detail(content_url)
        # print(content_url)
        # 设置抓取break间隙时间，减少请求对象服务器压力
        time.sleep(3)
        # break


# 解析内容详情页
def parse_detail(content_url):
    # pass
    # ----------------------------------------------------
    # 请求响应和获取
    resp = requests.get(content_url, headers=headers)
    text = resp.text
    text_parse = etree.HTML(text)
    # ----------------------------------------------------
    # 获取内容
    # 标题文本
    title = text_parse.xpath("//h1[@class='article-title']/text()")[0]
    # print(title)
    # ----------------------------------------------------
    # 内容文本
    content = text_parse.xpath("//div[@class='article-text']//text()")
    # ----------------------------------------------------
    # 整理内容文本
    thesis = "".join(content).strip().replace('\r\n\r\n\r\n\t','')
    thesis_pro = thesis.replace('\r\n','')
    # print(thesis)
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    # 替换 replace("space","")
    # ----------------------------------------------------
    # 正常输出结果是列表，需要用到join，整理文本格式
    # join示例
    # joke = ['a', 'b', 'c']
    # test = ''.join(joke)
    # print(test)
    # ----------------------------------------------------
    # 数据保存
    blank_list.append({
        'title': title,
        'content': thesis_pro
    })
    print(f"{blank_list}下载完毕！",end='\n')


# main主体运行测试
# 让模块（函数）可以自己单独执行（调试）,相当于构造了调用其它函数的入口，类似于C/C++里面的main函数了。
def main():
    # pass
    for page in range(1, 2):
        page_url = f"https://xiaohua.zol.com.cn/new/{page}.html"
        # 调用自定义的parse_page
        parse_page(page_url)
        # 设置抓取break间隙时间，减少请求对象服务器压力
        time.sleep(3)
        # break


# main() if 语句
# 若判断语句是通过的，执行判断条件里的main();
if __name__ == '__main__':
    main()

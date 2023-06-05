from bs4 import BeautifulSoup

# -----------------------------
# 搜索遍历树
"""
搜索遍历树，一般用得比较多的两种方法：
    find方法：         找到第一个满足条件的标签后就立即返回,只返回一个元素；
    find_all方法：     是把所有满足条件的标签选到，然后返回元素；
"""

# ---------------------
# 1.find 和 find_all方法


html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python 学习&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python 学习&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python 学习&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python 学习&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python 学习&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python 学习&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python 学习&tid=87&lid=2218">TEG11-高级AI开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>4</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python 学习&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python 学习&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a id="test" class="test" target='_blank' href="position_detail.php?id=34511&keywords=python 学习&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html, 'lxml')
# -----------------------
# 1. 获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('-'*50)
#
# -----------------------
# 2. 获取第2个tr标签
# tr = soup.find_all('tr',limit=2)   # 设置limit参数，查找”前两个“ tr标签
# print(tr)
# for tr in trs:
#     print(tr)
#     print('-'*50)

# -----------------------
# 3. 获取所有class等于even的tr标签
# trs = soup.find_all('tr', class_='even')
# trs = soup.find_all('tr', attrs={'class': 'even'})
# for tr in trs:
#     print(tr)
#     print('-' * 50)

# -----------------------
# 4. 将所有id等于test，class也等于test的a标签提取出来。
# list_ = soup.find_all('a', id='test', class_='test')
# for a in list_:
#     print(a)

# -----------------------
# 5. 获取所有a标签的href属性
"""
使用find和find_all的过滤条件：
    1.关键字参数：将属性的名字作为关键字参数的名字，以及属性的值作为关键字参数的值进行过滤；
    2.attrs参数：将属性条件放到一个字典中，传给attrs参数
"""

# alist = soup.find_all('a')
# for a in alist:
#       # 第一种方法：关键字参数
#     href = a['href']
#     print(href)
#       # 第二种方法：attrs参数
#     href = a.attrs['href']
#     print(href)

# ------------------------------------------------------------------
# 举例：获取所有的职位信息（纯文本）

# 1.查找tr标签，第一个除外，切片读取
trs = soup.find_all('tr')[1:]
lists = []

# 2.对tr标签进行遍历
for tr in trs:
    # 创建空白字典，用来存放内容
    info = {}
    # 查找tr标签内容下的td标签
    # tds = tr.find_all('td')
    # name = tds[0].string      # td标签内的字符串内容
    # category = tds[1].string      # category 类别
    # info['name'] = name
    # info['category'] = category

    # -----------------------------------
    # infos = list(tr.strings)
    # infos = list(tr.stripped_strings)     # 去除换行符等符号
    infos = tr.get_text()
    print(infos)

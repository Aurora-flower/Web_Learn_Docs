# urlretrieve函数：
#       urlretrieve(url,fileName)
#   可以方便的将网页上的一个文件保存到本地。

# ----------------------------------------------
# 实例：将url下载到本地
from urllib import request

# 可以下载源代码:
#       request.urlretrieve(url, file_name)  # 将网页文件保存到本地

# Ctrl + mouse left 查看内置函数内容

# ----------------------------------------------
# 可以下载图片
url = "https://cdn-ali-img-shstaticbz.shanhutech.cn/bizhi/staticwp/202109/a31e61a8d55d87b5a729d8643ef60929--4198607505.jpg"
request.urlretrieve(url, "real.jpg")

# 编码
"""
ASCII码-8
    8位二进制表示一个字符, 可以表示2^8个字符
    能够表示字母、数字等

GB2312 国标/GBK
UNICODE 万国码，统一编码
UTF-8

摩斯密码：
    由点dot(.)划dash(-)这两种符号组成
    sos
"""

# 常用库
"""
os          提供了大量操作文件、目录的方法
pathlib2    文件系统路径操作
openpyxl    操作excel文件
python 学习-docx 操作word文件
python 学习-pptx 操作PowerPoint文件
opencv-python 学习 图像处理模块，提供了强大的图像相关功能
"""

# ---------------------------------------------------------------
# 打开文件：
"""
文件读写之前需要打开文件，确定文件的读写模式。open()函数可以打开一个文件供读取或写入。

open函数语法如下：
    file_obj = open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
        ·file: 必需，文件路径(相对或绝对路径)
        ·open函数使用一个文件名作为唯一的强制参数，然后返回一个文件对象。
        ·模式（mode）和缓冲区（buffering）参数都是可选的，默认模式是读模式，默认缓冲区是无。
        
文件缓冲区:
    open()函数中第三个可选参数buffering控制着文件的缓冲。
    如果参数是0，I/O操作就是无缓冲的，直接将数据写到硬盘上；
    如果参数是1，I/O操作就是有缓冲的，数据先写到内存里，只有使用flush函数或者close函数才会将数据更新到硬盘；
    如果参数为大于1的数字则代表缓冲区的大小（单位是字节），-1（或者是任何负数）代表使用默认缓冲区的大小。
"""
# 打开一个文件，并返回对象，在对文件进行处理过程都需要使用打开文件后操作
file_obj = open('lesson.txt', mode='r')
file_obj.close()  # 使用open()方法一定要保证关闭文件对象，即调用close()方法

# -----------------------------------------
"""             
module:
      'r'  -- 读取文件read
      'w'  -- 写入文件witter,覆盖原有内容
      'a'  -- append，在文件尾部追加内容
      'b'  -- binary，二进制文件(图像内容、binary)
      't'  -- 默认的，打开txt文本文件(.txt)
      '+'  -- 复合,打开文件供更新用。(r+: 读写、写入时从头开始覆盖; w+:读写、清空源文件后读写 )
"""

# ---------------------------------------------------------------

# 关闭文件：
# 使用open()方法一定要保证关闭文件对象，即调用close()方法
#           file.close()

# 使用with...as...,隐式调用close()方法关闭文件
#           with open("file.txt",'r')as f:

#    文件关闭后，文件不能再进行读写操作。
#  file.closed:    判断文件是否已经关闭

# ---------------------------------------------------------------

# 文件属性
# file.name: 返回文件的名称
# file.mode: 返回打开文件时，采用的文件打开模式
# file.encoding: 返回打开文件时使用的编码格式;


# 注意：文件名，文件不在一个文件目录下，输入绝对文件路径可查; 同一目录下，文件名即可。

# Python提供了一种简单的写法，使用with语句来替代try...finally代码块和close
# with属性
with open("lesson.txt", 'r') as f:
    print(f.name)
    print(f.mode)
    print(f.encoding)
    print(f.closed)
f.close()
print(f.closed)
#  cp936其实就是GBK,IBM在发明code page的时候将GBK放在第936页

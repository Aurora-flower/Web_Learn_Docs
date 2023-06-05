# 安装 Excel相关的库
# pip install xlrd # 用于读
# pip install xlwt # 用于写

import xlrd
import xlwt
import random

# -------------------------------------------------------------------------------------
# 打开 Excel文件：
# xlrd.open_workbook(“abc.xls”)

# 获取 Sheet：
#   一个 Excel中可能有多个 Sheet，那么可以通过以下方法来获取想要的 Sheet信息：
"""    
    * 1. sheet_names：   获取所有的 sheet的名字。
    * 2. sheet_by_index：    根据索引获取 sheet对象。
    * 3. sheet_by_name： 根据名字获取 sheet对象。
    * 4. sheets：    获取所有的 sheet对象。
    * 5. sheet.nrows：   这个 sheet中的行数。
    * 6. sheet.ncols：   这个 sheet中的列数。
"""

# 读取 Excel 文件
workbook = xlrd.open_workbook("资产分析.xlsx")

# 获取所有的 sheet的名字
print(workbook.sheet_names())

"""
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * *问题报错：                                               * * *
# * * *  XLRDError: Excel xlsx file; not supported.            * * *
# * * *                                                        * * *
# * * *可能性：                                                 * * *
# * * *  新版本的xlrd只支持 xls文件                               * * *
# * * *                                                        * * *
# * * *解决方法：                                                * * *
# * * *  1.安装旧版本 xlrd                                       * * *
# * * *      >>> pip3 install xlrd==1.2.0                       * * *
# * * *  2.使用 openpyxl 代替 xlrd                               * * *
# * * *      >>> pip3 install openpyxl                          * * *
# * * *      指定  engine为 openpyxl                             * * *
# * * *      >>> pd.read_excel('xxxx.xlsx', engine='openpyxl')  * * *
# * * *                                                         * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

# 根据索引获取指定的 sheet对象
sheet = workbook.sheet_by_index(1)
print(sheet.name)

# 根据名称获取指定的 sheet对象
sheet = workbook.sheet_by_name("资产管家")
print(sheet.name)

# 获取所有的sheet对象
sheets = workbook.sheets()
for sheet in sheets:
    print(sheet.name)

# 获取指定sheet的行数和列数
sheet = workbook.sheet_by_index(0)
print({"rows 行": sheet.nrows, "cols 列": sheet.ncols})

# -------------------------------------------------------------------------------------
# Cell相关的操作：
#   每个 Cell代表的是表格中的一格。以下方法可以方便获取想要的 cell

"""
    * 1. sheet.cell(row,col)：   获取指定行和列的cell对象。
    * 2. sheet.row_slice(row,start_col,end_col)：    获取指定行的某几列的cell对象。
    * 3. sheet.col_slice(col,start_row,end_row)：    获取指定列的某几行的cell对象。
    * 4. sheet.cell_value(row,col)：     获取指定行和列的值。
    * 5. sheet.row_values(row,start_col,end_col)：   获取指定行的某几列的值。
    * 6. sheet.col_values(col,start_row,end_row)：   获取指定列的某几行的值。
"""

# -------------------------------------------------------------------------------------
# 获取指定行和列的cell对象
sheet = workbook.sheet_by_index(0)
cell = sheet.cell(3, 48)
print("总资产：%s" % cell)
print(f"总资产：{cell.value}")

# 获取指定行的某几列的cell对象
cell = sheet.row_slice(3, 1, 5)
print(f"第三行的2-4列：{cell}")

# 获取指定列的某几行的cell对象
cell = sheet.col_slice(3, 0, 4)  # empty 空
print(f"第三列的0-4行：{cell}")

# 获取指定行和列的值。
cell = sheet.cell_value(3, 1)
print(f"第4行第2列：{cell}")

# 获取指定行的某几列的值。
cell = sheet.row_values(3, 5, 9)
print(f"第4行第6-8列的值：{cell}")

# 获取指定列的某几行的值。
cell = sheet.col_values(4, 2, 4)
print(f"第5列第3-4行的值：{cell}")
# -------------------------------------------------------------------------------------
# 写入 Excel文件：
"""
Cell的数据类型：
    1. xlrd.XL_CELL_TEXT（Text）：     文本类型。
    2. xlrd.XL_CELL_NUMBER（Number）： 数值类型。
    3. xlrd.XL_CELL_DATE（Date）：     日期时间类型。
    4. xlrd.XL_CELL_BOOLEAN（Bool）：  布尔类型。
    5. xlrd.XL_CELL_EMPTY：           空白数据类型。
"""
sheet = workbook.sheet_by_index(0)
cell = sheet.cell(2, 3)
print("类型：", cell.ctype)  # 可以得到 cell 的类型
print(xlrd.XL_CELL_TEXT)

# callable 调用
"""
写入Excel步骤如下：
    1. 导入xlwt模块。
    2. 创建一个Workbook对象。
    3. 创建一个Sheet对象。
    4. 把数据写入到Sheet下指定行和列中。如果想要在原来workbook对象上添加新的cell，那么需
    要调用put_cell来添加。
    5. 保存成Excel文件。
"""
# 示例代码如下：
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheet1")
headers = ["姓名", "荷花", "支付宝", "银行卡", "微信", "总和"]
for index, header in enumerate(headers):
    # sheet.write(row,col,content)
    sheet.write(0, index, header)

names = ["张三", "李四", "王五", "王六"]
for index, name in enumerate(names):
    sheet.write(index + 1, 0, name)

for row in range(1, 5):
    for col in range(1, 5):
        sheet.write(row, col, random.randint(0, 10001))

workbook.save("资产表.xls")

# -------------------------------------------------------------------------------------
# 编辑 Excel文件：
rwb = xlrd.open_workbook("资产表.xls")
r_sheet = rwb.sheet_by_index(0)

r_sheet.put_cell(0, 5, xlrd.XL_CELL_TEXT, "总和", None)

# nrows = r_sheet.nrows
# ncols = r_sheet.ncols
# print(nrows, ncols)
for row in range(1, r_sheet.nrows):
    balance = r_sheet.row_values(row, 1, 4)
    # print(f'金额{balance}')
    total = sum(balance)
    r_sheet.put_cell(row, 5, xlrd.XL_CELL_NUMBER, total, None)  # 此时，还未存储

wr_asset = xlwt.Workbook()
money_sheet = wr_asset.add_sheet("sheet1")

for row in range(0, r_sheet.nrows):
    for col in range(0, r_sheet.ncols):
        money_sheet.write(row, col, r_sheet.cell_value(row, col))  # 相当于拷贝

wr_asset.save("资产表.xls")

"""
问题：
    以xlsx格式保存，打开则显示文件损坏或格式错误。
"""

# -------------------------------------------------------------------------------------

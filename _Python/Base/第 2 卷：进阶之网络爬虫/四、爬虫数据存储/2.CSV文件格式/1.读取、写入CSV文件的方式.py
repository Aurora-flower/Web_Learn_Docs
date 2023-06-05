import csv

# -------------------------------------------------------------------------------------
# 读取CSV文件的两种方式:

with open("stock.csv", 'r', encoding="GBK") as fp:
    # 读取到的每一条数据是一个列表，需要通过下标的方式获取具体某一个值
    # reader = csv.reader(fp)
    # for x in reader:
    #     print(x[3])

    # 读取到的每一条数据是一个字典，可以通过列名获取数据
    reader = csv.DictReader(fp)
    for x in reader:
        print(x['secShortName'])

# -------------------------------------------------------------------------------------
# 写入CSV文件的两种方式:

headers = ('name', 'age', 'weight', 'height')
students = [('平安', '13', '79', '135'),
            ('深振', '17', '130', '180'),
            ('美丽', '8', '60', '115')]
with open("students.csv", 'w', encoding="GBK", newline='') as fp:
    # newline=''，表示新的一行，不进行换行
    writer = csv.writer(fp)
    writer.writerow(headers)

    # 循环单行写入
    # for data in students:
    #     writer.writerow(data)

    # 多行写入
    writer.writerows(students)

    # 字典形式写入
    # 虽然DictWriter创建的时候有一个headers，但是想要写入数据进去，还是需要调用
    # writer.writeheader()方法，否则，表头数据写入不进去
    students = [
        {"name": "张三", "age": 18, "height": 180},
        {"name": "李四", "age": 19, "height": 190},
        {"name": "王五", "age": 20, "height": 170}
    ]
    writer = csv.DictWriter(fp, headers)
    writer.writeheader()
    writer.writerows(students)

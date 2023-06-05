# 程序调试： 对功能、程序等进行调整和实验验证。

# 编好程序后，用各种手段进行查错和排错的过程。
# 作为程序的正确性，不仅仅表现在正常功能的完成上，
# 更重要的是对意外情况的正确处理。

# print语句
for i in range(1, 5):
    # print(i)
    print("hello")

# assert 断言
n = 1
assert n != 0, "发生除数为0的错误"
print(5/n)

# 断点
# pycharm 点击左侧，F9
for i in range(2, 6):
    print(i)  # 单步执行


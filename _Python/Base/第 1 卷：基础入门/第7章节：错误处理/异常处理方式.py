# try_except捕获异常
try:
    print(8/0)
    # except 除了,扩展
except ZeroDivisionError as e:
    print("出现了除数为0的情况")
    print(ZeroDivisionError)
    print(e)
# 使用try-except语句，不影响程序的运行，后续的语句看可以运行
print('hello world')

# try_except捕获多个异常
try:
    print(5/0)
    print(t/2)
except ZeroDivisionError:
    print("除数不能为0")
except NameError:
    print("变量未定义")

try:
    print(b/2)
    print(5/0)
except ZeroDivisionError:
    print("除数不能为0")
except NameError:
    print("变量未定义")

# try_except-else捕获异常
try:
    x = 8/1
except ZeroDivisionError:
    print("除数为0")
else:
    print("x=", x)

# finally语句
try:
    y = 15/6
except ZeroDivisionError:
    print("除数为0")
else:
    print("x的值为", x)
finally:
    print("最后！")

print('hello')

# 逻辑与，运算符and

"""用户 user ； 密码 password
当用户输入了正确的用户名与密码，用户可以登录；
否则，提示非法用户"""

user = input("请输入您的用户名：")
password = input("请输入您的密码：")
if user == "YanBin" and password == "1234":
    print("欢迎登录")
else:
    print("请输入正确的用户名和密码")

# 逻辑或者，运算符or
'''
年龄小于16，或大于60岁，免门票
否则，买票去！
'''
# free 免费， ticket 门票
age = 17
if age < 16 or age > 60:
    print("free")
else:
    print("Fares, please!")  # 请买票!
'''
fare
(飞机)票价；车费；船费；出租车乘客；饭菜
成功(或不成功、更好等)
'''

# 逻辑非，运算符not
'''
年龄小于18岁，则不能购买烟酒，
否则，可以购买。
'''
age1 = 19
if not age1 < 18:
    print("please pay")  # payment 支付
else:
    print("Refuse to buy")   # Refuse to buy 拒绝购买
# Not for sale （no sale） 不卖！

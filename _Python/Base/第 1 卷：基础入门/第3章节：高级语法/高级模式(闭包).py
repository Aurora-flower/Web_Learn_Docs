"""
电子秤
可以计算：
        价格 = (毛重 - 包装重量) * 单价
        包装重量: 0.1 kg
        价格 = (毛重  - 0.1) * 单价
    # 苹果 ： 3 元/斤
    # 香蕉 ： 5 元/斤
Electronic scales
Can calculate.
        Price = (gross weight - package weight) * unit price
        Package weight: 0.1 kg
        Price = (gross weight - 0.1) * unit price
    # Apples: 3 yuan / catty
    # Banana: 5 yuan / catty
"""

# what = input("请输入你要买什么？")
# # apple ，banana
# # 苹果每1斤1个包装袋
# # 香蕉每1斤0.5个包装袋
#
# buy = input("你需要多少斤？")
# catty = float(buy)
# # catty
# if what == "apple":
#     package = catty * 1
#     unit = 3
# elif what == "both":
#     package = catty * 0.7
# else:
#     package = catty * 0.5
#     unit = 5
# package_weight = package * 0.1
# # print(package_weight)
#
#
# def price(gross_weight, unit_price):
#     net_weight = gross_weight - package_weight
#     return net_weight * unit_price
#
#
# total_scales = input("请确认电子秤显示重量:")
# scales = float(total_scales)
# money = price(scales, unit)
# print(money)
#

# def price(weight, unit_price):
#     return (weight - 0.1) * unit_price
#
#
# apple = price(10.1, 3)
# print(apple)
#
# banana = price(10.1, 5)
# print(banana)


# 闭包，函数里嵌函数
# 闭包：一个函数和对其周围状态（ lexical environment，词法环境 ）的引用捆绑在一起（或者说函数被引用包围），
# 这样的组合就是 闭包 （ closure ）。
def price(unitPrice):
    def computer(weight):
        return (weight - 0.1) * unitPrice
    return computer


apple = price(3)   # 不执行，引用
print(apple(10.1))
banana = price(5)
print(banana(10.1))

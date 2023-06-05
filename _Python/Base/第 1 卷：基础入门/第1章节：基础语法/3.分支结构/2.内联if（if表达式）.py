# 内联if（if表达式/if函数）
"""
语法规则：
        值1 if 条件 else 值2
                先对条件进行判断；
             条件成立，返回值1；否则，返回值2.
"""
# 使用if表达式，判断一个数的奇偶性
number = -6
# print("偶数") if number % 2 == 0 else print("奇数")
print("奇数") if number % 2 else print("偶数")  # 默认为0


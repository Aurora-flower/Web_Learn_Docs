"""
    基本 while循环:
      while 条件表达句：
            循环体
条件为真时，运行循环体；
需要注意的是，最后要让[条件表达式]不成立；否则，为死循环。[ctrl+c]终端
"""

# terminate 结束

# 输入姓名案例:
name = input('请输入姓名:')
while not name:
    name = input("姓名不能为空!请输入用户名:")
print("hello", name)

# ----------------------------------------------------------
# Unicode 统一字符编码，内码；
# while遍历

# 将奇数偶数分开
# Odd number 奇数； even numbers 偶数；
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []   # 偶数
odd = []    # 奇数
p = 0
while p < len(n):
    if n[p] % 2 == 0:  # inspection 检查; instead 相反，代替；
        even.append(n[p])  # 将a放到偶数序列内
    else:
        odd.append(n[p])  # 将a放到奇数序列内
    p += 1
print(even)
print(odd)
# 以上，是逐个相加的方法


# --------------------------
m = [13, 87, 94, 65, 49, 46, 55, 67, 66]
even = []
odd = []
while len(m) > 0:  # import 引进，输入；  invalid syntax 无效语法；
    b = m.pop()  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    if b % 2 == 0:
        even.append(b)
    else:
        odd.append(b)
print("偶数", even)
print("奇数", odd)
# 以上，是随机抽取的方法

# --------------------------------------------------------------
# 采用 while True循环语句：
#   采用该语句的核心思想是如果出现错误的话，可以继续循环。
#   while True 语句中一定要有结束该循环的break语句，否则会一直循环下去的。


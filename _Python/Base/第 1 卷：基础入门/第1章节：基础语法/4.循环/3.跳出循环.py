# 跳出循环 break 指令,彻底终结（强制离开 for循环）

"""
    循环（while或for-in)：
        if表达式
            break
break语句：结束循环，完成结束一个循环，跳出循环体。
核心要义：不需要完成整个循环。
"""

x = [56, 57, 87, 65, 98, 0, 79, 64]
flag = 0  # flag 旗帜，标志，标记;
number = 0
for a in x:
    if a == 0:
        flag = 1
    number += 1
    if flag == 1:
        print("列表里面有0", '循环第', number, '次')
    else:
        print("列表里没有0", '循环第', number, '次')

# 在没有break的情况下，遍历整个列表；
y = [44, 87, 78, 0, 54, 68, 87, 77, 98]
flag = 0
for i in y:
    if i == 0:
        flag = 1
        break  # 以break进行优化，减少运算量；
    # 因为是遍历列表，通过运算结果可以看出。
    if flag == 1:
        print('遇见了0')
    else:
        print('没遇到0')

# -----------------------------------------------------
# 跳出循环continue，暂时终结（for循环暂时停止不往下执行）
'''
循环（while或for-in）
    if表达式
        continue
continue:结束循环，忽略当次循环的剩下语句，从下一次执行；
核心要义：本次循环的后续不执行了，从下一轮继续；
'''

# 输出值得关注的值
a = [34, 48, 57, 98, 64, 324, 57, 45, 53, 21]
for r in a:
    if 0 <= r <= 100:
        continue
    print('请关注异常值：', r)

# -----------------------------------------------------
# for-else语句
"""
for 变量 in 对象:
    程序区块码1
    if 条件表达式:       # 条件表达式为ture，则离开for循环
        程序代码区块2
        break
    程序代码区块3
else:
    程序代码区块4         # 最后一次循环条件表达式为false则执行

"""
# 质数测试
num = int(input('请输入大于1的整数做质数测试：'))
if num == 2:
    print("%d是质数" % num)
else:
    for n in range(2, num):
        if num % n == 0:
            print("%d不是质数" % num)
            break
    else:
        print("%d是质数" % num)

# -----------------------------------------------------
# 作业：输出一个列表内，所有的被3整除的数
f = [1, 3, 9, 12, 78, 46, 18, 44, 79]
for h in f:
    if h % 3 == 0:
        print(h)
        # continue
        break

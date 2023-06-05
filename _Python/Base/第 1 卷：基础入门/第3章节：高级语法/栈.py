from collections import deque
"""
# 栈（先进先出）和队列（后进先出）

# 后进先出  last-in,first-out(LIFO)
应用场景：
    # 操作回退： Ctrl + Z
    # 数据库系统等场景
    # 浏览器回退上一页
    # 括号匹配

# 先进先出  first-in,last-out,(FIFO)
应用场景：
    # 历史记录：最早生成的，最早丢弃
    # 数据备份：最先生成的，最先丢弃
    # 打印机控制
    # CPU分配等
"""

# 栈的实现
# append,pop
x = [9, 7, 8]
print(x, end=',')
x.append(5)
print(x, end=',')
x.pop()
print(x, end='\n')

# 队列的实现
# collections收藏
variable = deque([9, 7, 8])   # queue 队列
print(variable, end=";")
variable.append(12)
print(variable, end=";")
variable.popleft()
print(variable, end="\n")

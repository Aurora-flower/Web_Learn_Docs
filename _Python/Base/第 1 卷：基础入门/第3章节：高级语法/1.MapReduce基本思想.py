# MapReduce是一种编程模型，用于大规模数据集（大于1TB）的并行运算。
# 它们的主要思想，都是从函数式编程语言里借来的。
# 每次一个步骤方法会产生一个状态，这个状态会直接当参数传进下一步中，而不是使用全局变量。
#

# MapReduce框架:
#   将复杂的，运行大规模集群上的并行计算过程高度地抽象两个函数：
#           Map和Reduce
#   采用“分而治之”策略:
#           将一个分布式文件系统中的大规模数据集，分成许多独立的分片。这些分片可以被多个Map任务并行处理。

# MapReduce设计的一个理念就是“计算向数据靠拢”，而不是“数据向计算靠拢”，
# 原因是，移动数据需要大量的网络传输开销


from functools import reduce

# Map 拆分
# Reduce 合并


def fun(var):
    return var * var


var_list = [1, 2, 3, 4, 5, 6, 7]
variable = map(fun, var_list)
print(list(variable))    # map(5.函数，列表)


def maximum(a, b):
    return a if a > b else b


form = [13, 23, 45, 67, 28, 19]
table = reduce(maximum, form)  # reduce(5.函数，列表)
print(table)
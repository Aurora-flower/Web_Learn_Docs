# 堆的定义
# 一棵完全二叉树的数组对象。

# 堆的特点
# 是完全二叉树；
# 用数组实现：将二叉树的结点按层级顺序放入数组，根节点在位置1，
# 它的子节点在位置2和3，子节点的子节点在4、5、6、7，以此类推；


# 父（根）节点的值只会小于或等于所有子节点（的值）
# 数组实现：从零开始，对于所有的k都有heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]
# 即 每个节点的下级都有left——heap[2*k+1] 和 right——heap[2*k+2]
# 最小的元素总是在根节点：heap[0]
import heapq

test = [7, 9, 4, 3, 5, 6]
print("list列表:", test)
# Name by word
# I'm learning English

heapq.heapify(test)
print("堆:", test)
# heapq.heapify()  将list 元素转换为 heap 堆

heapq.heappush(test, 2)
print("加入item值:", test)
# heapq.heappush(heap,item)   将item 的值加入heap中，保持堆的不变性

heapq.heappop(test)
print("弹出最小的item值，保持堆不变:", test)
# heapq.heappop(heap)
# 弹出并返回heap的最小元素，保持堆的不变性。
# 使用heap[0]，可以只访问最小的元素而不弹出它。


"""
# 交互（互动）5.函数

5.函数： 
        heapq.heappushpop(__heap,__item)     # push 推，推动
    注释：   将item放入堆中，然后弹出并返回heap的最小元素
            堆的大小保持不变
            先放进去，然后弹出来
    
        heapq.heapreplace(__heap,__item)     # replace 替换
    注释：   弹出并返回heap中最小的元素，同时推入新的item
            堆的大小不变
            先弹出来一个，再放一个
            “替换再排序”

"""
group = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]    # group 组
print("Primitive原始的:", group)          # Primitive, original   原始的，最初的
heapq.heapify(group)

print('先把group转换为堆形式:', group)
stack = heapq.heappushpop(group, 11)   # Pile/Heap/Stack 堆      Alternatives 替代品
print('弹出并返回heap的最小元素:', stack)
print("push推入的结果:", group)


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]    # group 组
print("original最初的", number)
heapq.heapify(number)

pile = heapq.heapreplace(number, 12)
print('弹出并返回heap中最小的元素:', pile)
print("replace替换的结果:", number)


"""
通用函数：
        heapq.merge(*iterables)      #  merge合并
    注释：   将多个'已排序'的而输入合并为一个已排序的输出。返回已排序的iterator迭代器
            例如：合并来自多个日志文件的带时间戳的条目        
            
        heapq.nlargest(n, iterable)   #  nlargest 最大者(的); iterable可迭代的
    注释：   从iterable所定义的数据集中返回前n个最大元素组成的列表。
    
        heapq.nsmallest(n, iterable)  #  nsmallest 最小者(的)
    注释：   从iterable所定义的数据集中返回前n个最小元素组成的列表。
"""

var_test = [3, 5, 7]
var_group = [1, 2, 4, 6]
sort = heapq.merge(var_test, var_group)   # sort 分类
print(list(sort))

# heapq --- 堆队列算法
# 官方文档：  https://docs.python.org/zh-cn/3/library/heapq.hetml

lst = [1, 432, 5, 435, 345, 56, 7, 6, 75, 8]
large_numbers = heapq.nlargest(4, lst)
small_numbers = heapq.nsmallest(4, lst)
print(large_numbers, small_numbers, sep=",")

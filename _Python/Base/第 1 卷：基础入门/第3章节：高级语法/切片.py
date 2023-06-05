# 切片的使用方法：
# 对象索引[开始索引:结束索引:步长]    三值都可以省略
#    index start_order:end_order:step         [start:stop) 左开右闭
#       正索引从0开始，负索引从-1开始
# omit 省略


# -------------------------------
# 访问：使用切片完成指定功能
lst = [23, 33, 4, 5, 56, 21]
print(lst[1])   # 切取单个对象
print(lst[::-1])  # 逆序 # 切取整个对象

code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(code[3:8][0:3][1])  # 多层切片
print(code[1::2])   # 取偶数索引位置的
print(code[1::2])   # 取奇数索引位置的

coding = [1, 2, 3, 4, 5, 6, 7, 8]
print(coding[:11])   # 结束索引超过列表长度，依旧是原来的list;开始索引超过列表长度则为空;

# -------------------------------
# 插入：使用切片插入元素值
list_var = [1, 2, 3, 4, 5, 6]
list_var[6:] = [7, 8, 9, 10]   # 插入
# variable[:0] = [value1, value2...]   # 首部插入元素
# variable[index:相同index] = [value1, value2...]  # 中间插入元素
# variable[end:] = [value1, value2...]  # 尾部插入元素
print(list_var)

# -------------------------------
# 修改：使用切片修改部分元素
replacement_list = [1, 3, 8, 10]
replacement_list[2:] = [5, 7]   # 替换，被替换长度与原替换长度相等
print(replacement_list)

repl_list = [1, 2, 3, 4, 5]
repl_list[3:] = [8, 7, 6]  # 替换，等号两侧，长度不一致
repl_list[2:4] = [0]
print(repl_list)

order = list(range(1, 10))
# order[::2] = ["换"]*5
order[1::2] = [0, 0, 0, 0, ]  # 替换，不相邻位置替换
# 注意：此时左右两边的长度要一致
print(order)

# -------------------------------
# 删除：使用切片删除部分元素
learn_lst = [1, 2, 3, 4, 5, 6]
learn_lst[2:4] = []   # {替换}删除   ---连续删除
print(learn_lst)

lst = [2, 4, 16, 2, 41, 67, 78]
del lst[1:2]   # delete 删除   ---连续删除
del lst[::2]    # ---间断删除
print(lst)


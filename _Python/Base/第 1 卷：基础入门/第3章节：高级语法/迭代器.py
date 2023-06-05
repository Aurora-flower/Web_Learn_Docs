
# 迭代器：
#       迭代器(iterator)是一中检查容器内元素并遍历元素的数据类型。
#       迭代器是一个可以记住遍历的位置的对象。
#       迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

# 可迭代对象：
#     列表/元组/集合/字典/字符串等对象称为可迭代对象
course = ['Math', 'English', 'Computer']
# iteration 迭代；iterators 迭代器
iteration = iter(course)   # iter() 创建迭代对象
print(next(iteration))     # next() 输出迭代器下一项
print(next(iteration))
print(next(iteration))

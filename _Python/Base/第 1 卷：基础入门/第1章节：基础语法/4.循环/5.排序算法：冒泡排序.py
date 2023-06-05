# 排序算法：冒泡排序
# 从第一个元素开始，往后比较相邻两个元素，按照需求进行交换(升序和降序)，经过多轮比较完成排序。
arr_one = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    bubble(arr_one),
    print(arr_one)

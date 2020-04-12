# 快速排序
import numpy as np


def partition(arr, low, high):
    i = (low-1)         # 最小元素索引
    pivot = arr[high]   # 定标点

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = np.random.permutation(1000)
n = len(arr)
print("array:")
for i in range(n):
    print("%d" % arr[i], end=", "),

quickSort(arr, 0, n-1)
print("\nsorted array:")
for i in range(n):
    print("%d" % arr[i], end=", "),

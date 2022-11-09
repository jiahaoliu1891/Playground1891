# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
from common import inputs

def insertSort(nums):
    N = len(nums)
    for i in range(N):
        # insert nums[j] in the right position
        j = i - 1
        curr = nums[i]
        while j >= 0 and nums[j] > curr:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = curr
    return nums


print(insertSort(inputs))

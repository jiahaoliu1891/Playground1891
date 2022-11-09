from common import inputs

"""
    O(N^2)
"""
def bubbleSort(nums):
    N = len(nums)
    for _ in range(N-1):
        for i in range(0, N-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

print(bubbleSort(inputs))
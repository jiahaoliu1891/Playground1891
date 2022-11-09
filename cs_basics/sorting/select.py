from common import inputs

def selectSort(nums):
    N = len(nums)
    for i in range(0, N-1): 
        min_idx = i
        for j in range(i+1, N):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # swap min_idx and i
        if min_idx != i:
            nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums

print(selectSort(inputs))
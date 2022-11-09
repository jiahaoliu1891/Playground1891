from common import inputs

# Space O(N)
# Time O(NlogN)

def mergeSort(nums):
    N = len(nums)
    # split [0, mid] [mid+1, N-1]
    if N < 2:
        return nums
    mid = N // 2
    left, right = nums[0:mid], nums[mid:]
    return merge(mergeSort(left), mergeSort(right))
    

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result = result + left
    if right:
        result = result + right
    return result

print(mergeSort(inputs))

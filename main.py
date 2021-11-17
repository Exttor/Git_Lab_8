def kbig(nums, k):
    for i in range(k - 1):
        nums.remove(max(nums))
    return max(nums)

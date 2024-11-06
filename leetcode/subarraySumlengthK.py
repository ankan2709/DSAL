def subarray_fixed_sum(nums, k):

    curr_sum = sum(nums[:k])

    for right in range(k, len(nums)):
        left = right - k
        curr_sum = max(curr_sum, sum(nums[left:right]))

    return curr_sum

nums = [1, 2, 3, 7, 4, 1]
k = 3
print(subarray_fixed_sum(nums, k))
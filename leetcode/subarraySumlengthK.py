def subarray_fixed_sum(nums, k):

    max_sum = sum(nums[:k])
    curr_sum = max_sum
    for right in range(k, len(nums)):
        left = right - k
        curr_sum -= nums[left]
        curr_sum += nums[right]
        max_sum = max(max_sum, curr_sum)

    return max_sum

nums = [1, 2, 3, 7, 4, 1]
k = 3
print(subarray_fixed_sum(nums, k))
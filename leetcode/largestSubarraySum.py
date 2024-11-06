def largestSubarraySum(nums, target):
    total = 0
    max_length = 0
    left = 0

    for right in range(len(nums)):
        total += nums[right]
        while total > target:
            total -= nums[left]
            left += 1
        max_length = max(max_length, right - left + 1)

        
        
    return max_length

nums = [1, 6, 3, 1, 2, 4, 5]
target = 10
print(largestSubarraySum(nums, target))
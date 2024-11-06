def smallestSubarray(nums, target):
    left = 0
    length = float('inf')
    total = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            length = min(length, right - left + 1)
            total -= nums[left]
            left += 1
        
    return length


nums = [1, 4, 1, 7, 3, 0, 2, 5]
target = 10
print(smallestSubarray(nums, target))
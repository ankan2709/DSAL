def twoSumSorted(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        curr_sum = nums[l] + nums[r]
        if curr_sum == target:
            return (l+1 , r+1)
        elif curr_sum > target:
            r -= 1
        else:
            l += 1
    return -1

print(twoSumSorted([2,7,11,15], 9))
print(twoSumSorted([2,3,4], 6))
print(twoSumSorted([-1,0],-1))
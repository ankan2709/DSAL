def removeDuplicates(nums):
    slow = 0
    fast = 0

    while fast < len(nums) - 1:
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    return nums[:slow+1] 

nums = [0,0,1,1,1,2,2]

print(removeDuplicates(nums))
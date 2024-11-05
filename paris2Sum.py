def find_2sum(nums, target):
    if len(nums) <= 1:
        return []
    res = []
    i, j = 0, len(nums) - 1

    while i < j:

        total = nums[i] + nums[j]
        if total == target:
            res.append([nums[i], nums[j]])

            i += 1
            j -= 1

            while i < j and nums[i] == nums[i - 1]:
                i += 1

            while i < j and nums[j] == nums[j + 1]:
                j -= 1

        elif total < target:
            i += 1
        else:
            j -= 1

    return res

nums = [-1,0,0,1,2,2,7]
nums.sort()
# target =  0
# result = find_2sum(nums, 1)
# print(result)

def missingNum(nums):
    total = sum([x for x in range(len(nums)+1)])
    currTotal = sum(nums)

    return total - currTotal
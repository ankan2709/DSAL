from collections import defaultdict

def subarraySumK(nums, k):

    prefix_sum = 0
    myMap = defaultdict(int)
    myMap[0] = -1 # storing the index of the prefix sum

    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum - k in myMap:
            return (myMap[prefix_sum - k] + 1, i)
        else:
            myMap[prefix_sum] = i

    return False
arr = [1, -20, -3, 30, 5, 4] 
target = 7
print(subarraySumK(arr, target))
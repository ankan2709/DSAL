import collections
def twoSum(nums, target):

    hashMap = collections.defaultdict(int)

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashMap:
            return [hashMap[complement], i]
        
        hashMap[nums[i]] = i
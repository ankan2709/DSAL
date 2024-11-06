import collections

def minCardsPickForPair(nums):
    myset = collections.defaultdict(int)
    left = 0
    res = float('inf')

    for right in range(len(nums)):
        myset[nums[right]] += 1
        while myset[nums[right]] == 2:
            res = min(res, right - left + 1)
            myset[nums[left]] -= 1
            left += 1
    return res

cards = [3, 4, 2, 3, 4, 7]
print(minCardsPickForPair(cards))
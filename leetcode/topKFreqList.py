import collections
import heapq
def topKFrequent(nums, k):

    hashmap = collections.defaultdict(int)

    for num in nums:
        hashmap[num] += 1

    heap = []

    for key, val in hashmap.items():

        heapq.heappush(heap, (val, key))

        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)
    
    return [key for _, key in heap]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
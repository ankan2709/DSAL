from heapq import heappush, heappop

def kthLargest(arr, k):
    heap = []

    for i in range(len(arr)):
        heappush(heap, arr[i])
        if len(heap) > k:
            heappop(heap)


    return heap[0]

arr = [3,2,1,5,6,4]
k = 2
print(kthLargest(arr, k))